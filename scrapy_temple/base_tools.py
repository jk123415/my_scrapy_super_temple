# -*- coding: utf-8 -*-


str = '_ga=GA1.2.1982356954.1552032482; _octo=GH1.1.1651166253.1552032483; has_recent_activity=1; tz=Asia%2FShanghai; user_session=YWu057qVFf4_J7TrIS1Bqvj8XdM-yf8V0pfafq5bJ8aArEv1; __Host-user_session_same_site=YWu057qVFf4_J7TrIS1Bqvj8XdM-yf8V0pfafq5bJ8aArEv1; logged_in=yes; dotcom_user=jk123415; _gh_sess=OGNkc3VINWRKUmYxeGZld01WL0Z3bDM1YVJmQnJCR0gwR3ZOK2N5VXhzVHJuNEtkWSt1RlIvejRKdEJPWGVxNEdRcHRHdkptY0dacEl4cXdkS3hJdUJKMjk2bVNmMC9Qc2VTRkZHNWdMcWFnR2J2U2RrZUYrdTdBVWJoZ1VaL0J1d3k5ZnNnVy9oay8rZkx5ZGxCS1RGdGRuUnFpSFNvT1ZWSGk0UVoxZ0thVnBTVHdNMmF5L0VLZEtEQlJOL3RrSVhNb09IckdlZXBOUGpvbGYyd3NNcDB2REJ3UDR0cW0wZnpoUjlHbmNWaHpYV0p5WDkwN1dycDcwMWMyRkZUVi0tZjdRbzhHbndzSnlDSXBIVmtybk1nQT09--a56d2afdc40d84d76b16628b001a4f24a62e9c10'

bb = dict([x.split('=') for x in str.split('; ')])
print(bb)
