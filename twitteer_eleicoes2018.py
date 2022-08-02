import argparse
from pipes import quote
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from soupsieve import escape

def trata_dados_twitter(data_source, output_uri):
    """
    Processes sample food establishment inspection data and queries the data to find the top 10 establishments
    with the most Red violations from 2006 to 2020.

    :param data_source: The URI of your food establishment data CSV, such as 's3://DOC-EXAMPLE-BUCKET/food-establishment-data.csv'.
    :param output_uri: The URI where output is written, such as 's3://DOC-EXAMPLE-BUCKET/restaurant_violation_results'.
    """
    with SparkSession.builder.appName("Trata dados vindo do Twitter").getOrCreate() as spark:
        # Load the restaurant violation CSV data
        if data_source is not None:
            df = spark.read.options(delimiter=";", header=True, quote="\"", escape="\"").csv(data_source)

            icon_positivo = [":D", ":)", ":]"]
            icon_negativo = [":(", ":[", ":["]    


            df = df\
                    .select(
                        df['id'],
                        df['tweet_text'],

                        

                        F.date_format(F.to_timestamp(df['tweet_date'], "yyyy-MM-dd HH:mm:ss"), "yyyy/MM/dd HH:mm:ss").alias('tweet_date'),
                        
                        F.when(df['tweet_text'].contains(icon_positivo[0]) == 'true', "Positivo")\
                            .when(df['tweet_text'].contains(icon_positivo[1]) == 'true', "Positivo")
                            .when(df['tweet_text'].contains(icon_positivo[2]) == 'true', "Positivo")
                            .when(df['tweet_text'].contains(icon_negativo[0]) == 'true', "Negativo")
                            .when(df['tweet_text'].contains(icon_negativo[1]) == 'true', "Negativo")
                            .when(df['tweet_text'].contains(icon_negativo[2]) == 'true', "Negativo")
                            .otherwise("Neutro")
                            .alias("Sentimento"),
                        
                        F.when(df['tweet_text'].contains(icon_positivo[0]) == 'true', icon_positivo[0])\
                            .when(df['tweet_text'].contains(icon_positivo[1]) == 'true', icon_positivo[1])
                            .when(df['tweet_text'].contains(icon_positivo[2]) == 'true', icon_positivo[2])
                            .when(df['tweet_text'].contains(icon_negativo[0]) == 'true', icon_negativo[0])
                            .when(df['tweet_text'].contains(icon_negativo[1]) == 'true', icon_negativo[1])
                            .when(df['tweet_text'].contains(icon_negativo[2]) == 'true', icon_negativo[2])
                            .otherwise("Neutro")
                            .alias("Simbolo")

                        )\
                    # .show(10)

            df.write.options(delimiter=";", header=True, quote="\"", escape="\"").mode(
                    "overwrite").parquet(output_uri)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--data_source', help="The URI for you CSV restaurant data, like an S3 bucket location.")
    parser.add_argument(
        '--output_uri', help="The URI where output is saved, like an S3 bucket location.")
    args = parser.parse_args()

    trata_dados_twitter(args.data_source, args.output_uri)
