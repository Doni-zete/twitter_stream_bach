# Configurando o GLUE JOB AWS para receber cargas streaming em tempo real do Twitter e historico dados brutos alocados em csv usando o AWS EMR

### Comando para executar no aws emr e na maquina local para fins de teste
[**Comando para executar no aws emr no campo arguments e tambem comandos para executar no terminal maquina local testes**](https://github.com/Doni-zete/python_compasso/blob/main/execucao_aws/comando_executar.txt)
### Codigo para colocar a coluna simbolo e sentimento, no arquivo csv pode converter para qualquer formato os aquivos.
[**twitteer_eleicoes2018.py**](https://github.com/Doni-zete/twitter_stream_bach/blob/main/twitteer_eleicoes2018.py)

### Entrada dos arquivos bruto em csv
[**twitteer_eleicoes2018_dados_brutos.csv**](https://github.com/Doni-zete/python_compasso/blob/main/execucao_aws/tweet_create_date2018.csv)

### Codigo para pegar em tempo real tweets e savar em bucket aws
[**script_para_pegar_dados_do_tweter_na_aws**](https://github.com/Doni-zete/python_compasso/blob/main/execucao_aws/script_para_pegar_dados_do_tweter_na_aws.py)





# Passo 1
![Glue-job](https://github.com/Doni-zete/twitter_stream_bach/blob/main/img-configuracao-job/job1.PNG)
# Passo 2
![Glue-job-passo2](https://github.com/Doni-zete/twitter_stream_bach/blob/main/img-configuracao-job/job2.PNG)
# Passo 3
![Glue-job-passo3](https://github.com/Doni-zete/twitter_stream_bach/blob/main/img-configuracao-job/job3.PNG)
# Passo 4
![Glue-job-passo4](https://github.com/Doni-zete/twitter_stream_bach/blob/main/img-configuracao-job/job4.PNG)
# Passo 5
![Glue-job-passo5](https://github.com/Doni-zete/twitter_stream_bach/blob/main/img-configuracao-job/job5.PNG)

# Passo 6 a mais importante
### O primeiro campo que aparece "key" e para passar o comando o segundo campo "value" e para passar a biblioteca que sera instalada
### [**Referência**](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-libraries.html)
### [**Bibliotecas que ja vem instaladas**](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-libraries.html#glue20-modules-provided)

![Glue-job-passo6](https://github.com/Doni-zete/python_compasso/blob/main/execucao_aws/img-configuracao-job/job_amais_IMPORTANTE.PNG)


# Visualização dos detalhes jobs
![Glue-job-passo7](https://github.com/Doni-zete/python_compasso/blob/main/execucao_aws/img-configuracao-job/detalhes.PNG)

# Configurando disparador schedule a cada 15 minutos
![Glue-job-passo8](https://github.com/Doni-zete/python_compasso/blob/main/execucao_aws/img-configuracao-job/configurando_disparador_schedule_a_cada15.PNG)

# Recebendo json do twitter em tempo real a cada 15 minutos
![Glue-job-passo9](https://github.com/Doni-zete/python_compasso/blob/main/execucao_aws/img-configuracao-job/dados-atualizando-acada10minutos.PNG)


