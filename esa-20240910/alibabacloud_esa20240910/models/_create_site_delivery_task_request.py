# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class CreateSiteDeliveryTaskRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        data_center: str = None,
        delivery_type: str = None,
        discard_rate: float = None,
        field_name: str = None,
        filter_ver: str = None,
        http_delivery: main_models.CreateSiteDeliveryTaskRequestHttpDelivery = None,
        kafka_delivery: main_models.CreateSiteDeliveryTaskRequestKafkaDelivery = None,
        oss_delivery: main_models.CreateSiteDeliveryTaskRequestOssDelivery = None,
        s_3delivery: main_models.CreateSiteDeliveryTaskRequestS3Delivery = None,
        site_id: int = None,
        sls_delivery: main_models.CreateSiteDeliveryTaskRequestSlsDelivery = None,
        task_name: str = None,
    ):
        # The log category. Valid values:
        # 
        # *   **dcdn_log_access_l1** (default): access logs.
        # *   **dcdn_log_er**: Edge Routine logs.
        # *   **dcdn_log_waf**: firewall logs.
        # *   **dcdn_log_ipa**: TCP/UDP proxy logs.
        # 
        # This parameter is required.
        self.business_type = business_type
        # The data center. Valid values:
        # 
        # *   cn: the Chinese mainland.
        # *   oversea: outside the Chinese mainland.
        self.data_center = data_center
        # The destination of the delivery. Valid values:
        # 
        # *   sls: Alibaba Cloud Simple Log Service (SLS).
        # *   http: HTTP server.
        # *   aws3: Amazon Simple Storage Service (S3).
        # *   oss: Alibaba Cloud Object Storage Service (OSS).
        # *   kafka: Kafka.
        # *   aws3cmpt: S3-compatible storage service.
        # 
        # This parameter is required.
        self.delivery_type = delivery_type
        # The discard rate. Default value: 0.
        self.discard_rate = discard_rate
        # The log fields, which are separated by commas (,).
        # 
        # This parameter is required.
        self.field_name = field_name
        self.filter_ver = filter_ver
        # The configurations for delivery to an HTTP server.
        self.http_delivery = http_delivery
        # The configurations for delivery to Kafka.
        self.kafka_delivery = kafka_delivery
        # The configurations for delivery to OSS.
        self.oss_delivery = oss_delivery
        # The configurations for delivery to Amazon S3 or an S3-compatible service.
        self.s_3delivery = s_3delivery
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The configurations for delivery to SLS.
        self.sls_delivery = sls_delivery
        # The name of the delivery task.
        # 
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        if self.http_delivery:
            self.http_delivery.validate()
        if self.kafka_delivery:
            self.kafka_delivery.validate()
        if self.oss_delivery:
            self.oss_delivery.validate()
        if self.s_3delivery:
            self.s_3delivery.validate()
        if self.sls_delivery:
            self.sls_delivery.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        if self.delivery_type is not None:
            result['DeliveryType'] = self.delivery_type

        if self.discard_rate is not None:
            result['DiscardRate'] = self.discard_rate

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.filter_ver is not None:
            result['FilterVer'] = self.filter_ver

        if self.http_delivery is not None:
            result['HttpDelivery'] = self.http_delivery.to_map()

        if self.kafka_delivery is not None:
            result['KafkaDelivery'] = self.kafka_delivery.to_map()

        if self.oss_delivery is not None:
            result['OssDelivery'] = self.oss_delivery.to_map()

        if self.s_3delivery is not None:
            result['S3Delivery'] = self.s_3delivery.to_map()

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.sls_delivery is not None:
            result['SlsDelivery'] = self.sls_delivery.to_map()

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('DeliveryType') is not None:
            self.delivery_type = m.get('DeliveryType')

        if m.get('DiscardRate') is not None:
            self.discard_rate = m.get('DiscardRate')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('FilterVer') is not None:
            self.filter_ver = m.get('FilterVer')

        if m.get('HttpDelivery') is not None:
            temp_model = main_models.CreateSiteDeliveryTaskRequestHttpDelivery()
            self.http_delivery = temp_model.from_map(m.get('HttpDelivery'))

        if m.get('KafkaDelivery') is not None:
            temp_model = main_models.CreateSiteDeliveryTaskRequestKafkaDelivery()
            self.kafka_delivery = temp_model.from_map(m.get('KafkaDelivery'))

        if m.get('OssDelivery') is not None:
            temp_model = main_models.CreateSiteDeliveryTaskRequestOssDelivery()
            self.oss_delivery = temp_model.from_map(m.get('OssDelivery'))

        if m.get('S3Delivery') is not None:
            temp_model = main_models.CreateSiteDeliveryTaskRequestS3Delivery()
            self.s_3delivery = temp_model.from_map(m.get('S3Delivery'))

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SlsDelivery') is not None:
            temp_model = main_models.CreateSiteDeliveryTaskRequestSlsDelivery()
            self.sls_delivery = temp_model.from_map(m.get('SlsDelivery'))

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

class CreateSiteDeliveryTaskRequestSlsDelivery(DaraModel):
    def __init__(
        self,
        slslog_store: str = None,
        slsproject: str = None,
        slsregion: str = None,
    ):
        # The name of the Logstore.
        self.slslog_store = slslog_store
        # The name of the SLS project.
        self.slsproject = slsproject
        # The region in which the SLS project resides.
        self.slsregion = slsregion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.slslog_store is not None:
            result['SLSLogStore'] = self.slslog_store

        if self.slsproject is not None:
            result['SLSProject'] = self.slsproject

        if self.slsregion is not None:
            result['SLSRegion'] = self.slsregion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SLSLogStore') is not None:
            self.slslog_store = m.get('SLSLogStore')

        if m.get('SLSProject') is not None:
            self.slsproject = m.get('SLSProject')

        if m.get('SLSRegion') is not None:
            self.slsregion = m.get('SLSRegion')

        return self

class CreateSiteDeliveryTaskRequestS3Delivery(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        bucket_path: str = None,
        endpoint: str = None,
        prefix_path: str = None,
        region: str = None,
        s_3cmpt: bool = None,
        secret_key: str = None,
        server_side_encryption: bool = None,
        vertify_type: str = None,
    ):
        # The access key ID of your Amazon S3 account.
        self.access_key = access_key
        # The directory in the bucket.
        self.bucket_path = bucket_path
        # The endpoint. This parameter is required when the S3Cmpt parameter is set to true.
        self.endpoint = endpoint
        # The prefix of the path in which you want to store logs.
        self.prefix_path = prefix_path
        # The region ID of the service.
        self.region = region
        # Specifies whether the service is compatible with Amazon S3.
        self.s_3cmpt = s_3cmpt
        # The secret access key of your Amazon S3 account.
        self.secret_key = secret_key
        self.server_side_encryption = server_side_encryption
        self.vertify_type = vertify_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.bucket_path is not None:
            result['BucketPath'] = self.bucket_path

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.prefix_path is not None:
            result['PrefixPath'] = self.prefix_path

        if self.region is not None:
            result['Region'] = self.region

        if self.s_3cmpt is not None:
            result['S3Cmpt'] = self.s_3cmpt

        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key

        if self.server_side_encryption is not None:
            result['ServerSideEncryption'] = self.server_side_encryption

        if self.vertify_type is not None:
            result['VertifyType'] = self.vertify_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('BucketPath') is not None:
            self.bucket_path = m.get('BucketPath')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('PrefixPath') is not None:
            self.prefix_path = m.get('PrefixPath')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('S3Cmpt') is not None:
            self.s_3cmpt = m.get('S3Cmpt')

        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')

        if m.get('ServerSideEncryption') is not None:
            self.server_side_encryption = m.get('ServerSideEncryption')

        if m.get('VertifyType') is not None:
            self.vertify_type = m.get('VertifyType')

        return self

class CreateSiteDeliveryTaskRequestOssDelivery(DaraModel):
    def __init__(
        self,
        aliuid: str = None,
        bucket_name: str = None,
        prefix_path: str = None,
        region: str = None,
    ):
        # The ID of your Alibaba Cloud account.
        self.aliuid = aliuid
        # The name of the OSS bucket.
        self.bucket_name = bucket_name
        # The prefix of the path in which you want to store logs.
        self.prefix_path = prefix_path
        # The region in which the bucket is located.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid

        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.prefix_path is not None:
            result['PrefixPath'] = self.prefix_path

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')

        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('PrefixPath') is not None:
            self.prefix_path = m.get('PrefixPath')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class CreateSiteDeliveryTaskRequestKafkaDelivery(DaraModel):
    def __init__(
        self,
        balancer: str = None,
        brokers: List[str] = None,
        compress: str = None,
        machanism_type: str = None,
        password: str = None,
        topic: str = None,
        user_auth: bool = None,
        user_name: str = None,
    ):
        # The load balancing method.
        self.balancer = balancer
        # The brokers.
        self.brokers = brokers
        # The compression method.
        self.compress = compress
        # The encryption method.
        self.machanism_type = machanism_type
        # The password.
        self.password = password
        # The topic.
        self.topic = topic
        # Specifies whether to enable authentication.
        self.user_auth = user_auth
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.balancer is not None:
            result['Balancer'] = self.balancer

        if self.brokers is not None:
            result['Brokers'] = self.brokers

        if self.compress is not None:
            result['Compress'] = self.compress

        if self.machanism_type is not None:
            result['MachanismType'] = self.machanism_type

        if self.password is not None:
            result['Password'] = self.password

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.user_auth is not None:
            result['UserAuth'] = self.user_auth

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Balancer') is not None:
            self.balancer = m.get('Balancer')

        if m.get('Brokers') is not None:
            self.brokers = m.get('Brokers')

        if m.get('Compress') is not None:
            self.compress = m.get('Compress')

        if m.get('MachanismType') is not None:
            self.machanism_type = m.get('MachanismType')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('UserAuth') is not None:
            self.user_auth = m.get('UserAuth')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class CreateSiteDeliveryTaskRequestHttpDelivery(DaraModel):
    def __init__(
        self,
        compress: str = None,
        dest_url: str = None,
        header_param: Dict[str, main_models.HttpDeliveryHeaderParamValue] = None,
        last_log_split: bool = None,
        log_body_prefix: str = None,
        log_body_suffix: str = None,
        log_split: bool = None,
        log_split_words: str = None,
        max_batch_mb: int = None,
        max_batch_size: int = None,
        max_retry: int = None,
        query_param: Dict[str, main_models.HttpDeliveryQueryParamValue] = None,
        standard_auth_on: bool = None,
        standard_auth_param: main_models.CreateSiteDeliveryTaskRequestHttpDeliveryStandardAuthParam = None,
        transform_timeout: int = None,
    ):
        # The compression method. By default, data is not compressed.
        self.compress = compress
        # The address of the HTTP server.
        self.dest_url = dest_url
        # The custom headers.
        self.header_param = header_param
        self.last_log_split = last_log_split
        # The prefix of the log delivery package.
        self.log_body_prefix = log_body_prefix
        # The suffix of the log delivery package.
        self.log_body_suffix = log_body_suffix
        self.log_split = log_split
        self.log_split_words = log_split_words
        # The maximum size of data for each delivery. Unit: MB.
        self.max_batch_mb = max_batch_mb
        # The maximum number of entries for each delivery.
        self.max_batch_size = max_batch_size
        # The maximum number of retries.
        self.max_retry = max_retry
        # The custom query parameters.
        self.query_param = query_param
        # Specifies whether to use server authentication.
        self.standard_auth_on = standard_auth_on
        # The authentication configurations.
        self.standard_auth_param = standard_auth_param
        # The timeout period. Unit: seconds.
        self.transform_timeout = transform_timeout

    def validate(self):
        if self.header_param:
            for v1 in self.header_param.values():
                 if v1:
                    v1.validate()
        if self.query_param:
            for v1 in self.query_param.values():
                 if v1:
                    v1.validate()
        if self.standard_auth_param:
            self.standard_auth_param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compress is not None:
            result['Compress'] = self.compress

        if self.dest_url is not None:
            result['DestUrl'] = self.dest_url

        result['HeaderParam'] = {}
        if self.header_param is not None:
            for k1, v1 in self.header_param.items():
                result['HeaderParam'][k1] = v1.to_map() if v1 else None

        if self.last_log_split is not None:
            result['LastLogSplit'] = self.last_log_split

        if self.log_body_prefix is not None:
            result['LogBodyPrefix'] = self.log_body_prefix

        if self.log_body_suffix is not None:
            result['LogBodySuffix'] = self.log_body_suffix

        if self.log_split is not None:
            result['LogSplit'] = self.log_split

        if self.log_split_words is not None:
            result['LogSplitWords'] = self.log_split_words

        if self.max_batch_mb is not None:
            result['MaxBatchMB'] = self.max_batch_mb

        if self.max_batch_size is not None:
            result['MaxBatchSize'] = self.max_batch_size

        if self.max_retry is not None:
            result['MaxRetry'] = self.max_retry

        result['QueryParam'] = {}
        if self.query_param is not None:
            for k1, v1 in self.query_param.items():
                result['QueryParam'][k1] = v1.to_map() if v1 else None

        if self.standard_auth_on is not None:
            result['StandardAuthOn'] = self.standard_auth_on

        if self.standard_auth_param is not None:
            result['StandardAuthParam'] = self.standard_auth_param.to_map()

        if self.transform_timeout is not None:
            result['TransformTimeout'] = self.transform_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compress') is not None:
            self.compress = m.get('Compress')

        if m.get('DestUrl') is not None:
            self.dest_url = m.get('DestUrl')

        self.header_param = {}
        if m.get('HeaderParam') is not None:
            for k1, v1 in m.get('HeaderParam').items():
                temp_model = main_models.HttpDeliveryHeaderParamValue()
                self.header_param[k1] = temp_model.from_map(v1)

        if m.get('LastLogSplit') is not None:
            self.last_log_split = m.get('LastLogSplit')

        if m.get('LogBodyPrefix') is not None:
            self.log_body_prefix = m.get('LogBodyPrefix')

        if m.get('LogBodySuffix') is not None:
            self.log_body_suffix = m.get('LogBodySuffix')

        if m.get('LogSplit') is not None:
            self.log_split = m.get('LogSplit')

        if m.get('LogSplitWords') is not None:
            self.log_split_words = m.get('LogSplitWords')

        if m.get('MaxBatchMB') is not None:
            self.max_batch_mb = m.get('MaxBatchMB')

        if m.get('MaxBatchSize') is not None:
            self.max_batch_size = m.get('MaxBatchSize')

        if m.get('MaxRetry') is not None:
            self.max_retry = m.get('MaxRetry')

        self.query_param = {}
        if m.get('QueryParam') is not None:
            for k1, v1 in m.get('QueryParam').items():
                temp_model = main_models.HttpDeliveryQueryParamValue()
                self.query_param[k1] = temp_model.from_map(v1)

        if m.get('StandardAuthOn') is not None:
            self.standard_auth_on = m.get('StandardAuthOn')

        if m.get('StandardAuthParam') is not None:
            temp_model = main_models.CreateSiteDeliveryTaskRequestHttpDeliveryStandardAuthParam()
            self.standard_auth_param = temp_model.from_map(m.get('StandardAuthParam'))

        if m.get('TransformTimeout') is not None:
            self.transform_timeout = m.get('TransformTimeout')

        return self

class CreateSiteDeliveryTaskRequestHttpDeliveryStandardAuthParam(DaraModel):
    def __init__(
        self,
        expired_time: int = None,
        private_key: str = None,
        url_path: str = None,
    ):
        # The validity period of the signature.
        # 
        # >  The value must be greater than 0. We recommend that you specify a value that is greater than 300.
        self.expired_time = expired_time
        # The private key.
        self.private_key = private_key
        # The URI path for server authentication.
        self.url_path = url_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.private_key is not None:
            result['PrivateKey'] = self.private_key

        if self.url_path is not None:
            result['UrlPath'] = self.url_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')

        if m.get('UrlPath') is not None:
            self.url_path = m.get('UrlPath')

        return self

