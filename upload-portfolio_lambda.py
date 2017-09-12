import boto3
s3 = boto3.resource('s3')
portfolio_bucket = s3.Bucket('portfolio.abhayrajan.info')
for obj in portfolio_bucket.objects.all():
    print obj.key
build_bucket = s3.Bucket('portfoliobuild.abhayrajan.info')
build_bucket.download_file('portfolioBuild.zip', '/tmp/portfolioBuild.zip')
import StringIO
portfolio_zip = StringIO.StringIO()
build_bucket.download_fileobj('portfolioBuild.zip', portfolio_zip)
import zipfile
with zipfile.ZipFile(portfolio_zip) as myzip:
    for nm in myzip.namelist()
with zipfile.ZipFile(portfolio_zip) as myzip:
    for nm in myzip.namelist():
        print nm
with zipfile.ZipFile(portfolio_zip) as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        portfolio_bucket.upload_fileobj(obj, nm)
with zipfile.ZipFile(portfolio_zip) as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        portfolio_bucket.upload_fileobj(obj, nm)
        portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
