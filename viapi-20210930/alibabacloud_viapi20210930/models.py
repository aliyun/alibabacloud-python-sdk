# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AiStoreUserTask(TeaModel):
    def __init__(
        self,
        api_desc: str = None,
        api_name: str = None,
        bucket_key_prefix: str = None,
        bucket_name: str = None,
        disable_time: str = None,
        enable_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        param_info: str = None,
        product: str = None,
        product_desc: str = None,
        receive_config: str = None,
        region: str = None,
        region_desc: str = None,
        remark: str = None,
        status: str = None,
        task_version: str = None,
        version: str = None,
    ):
        self.api_desc = api_desc
        self.api_name = api_name
        self.bucket_key_prefix = bucket_key_prefix
        self.bucket_name = bucket_name
        self.disable_time = disable_time
        self.enable_time = enable_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.name = name
        self.param_info = param_info
        self.product = product
        self.product_desc = product_desc
        self.receive_config = receive_config
        self.region = region
        self.region_desc = region_desc
        self.remark = remark
        self.status = status
        self.task_version = task_version
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_desc is not None:
            result['ApiDesc'] = self.api_desc
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.bucket_key_prefix is not None:
            result['BucketKeyPrefix'] = self.bucket_key_prefix
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.disable_time is not None:
            result['DisableTime'] = self.disable_time
        if self.enable_time is not None:
            result['EnableTime'] = self.enable_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.param_info is not None:
            result['ParamInfo'] = self.param_info
        if self.product is not None:
            result['Product'] = self.product
        if self.product_desc is not None:
            result['ProductDesc'] = self.product_desc
        if self.receive_config is not None:
            result['ReceiveConfig'] = self.receive_config
        if self.region is not None:
            result['Region'] = self.region
        if self.region_desc is not None:
            result['RegionDesc'] = self.region_desc
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.task_version is not None:
            result['TaskVersion'] = self.task_version
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDesc') is not None:
            self.api_desc = m.get('ApiDesc')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BucketKeyPrefix') is not None:
            self.bucket_key_prefix = m.get('BucketKeyPrefix')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('DisableTime') is not None:
            self.disable_time = m.get('DisableTime')
        if m.get('EnableTime') is not None:
            self.enable_time = m.get('EnableTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamInfo') is not None:
            self.param_info = m.get('ParamInfo')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ProductDesc') is not None:
            self.product_desc = m.get('ProductDesc')
        if m.get('ReceiveConfig') is not None:
            self.receive_config = m.get('ReceiveConfig')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionDesc') is not None:
            self.region_desc = m.get('RegionDesc')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskVersion') is not None:
            self.task_version = m.get('TaskVersion')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class AiStoreApiNode(TeaModel):
    def __init__(
        self,
        apis: List[AiStoreUserTask] = None,
        product: str = None,
        product_desc: str = None,
    ):
        self.apis = apis
        self.product = product
        self.product_desc = product_desc

    def validate(self):
        if self.apis:
            for k in self.apis:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Apis'] = []
        if self.apis is not None:
            for k in self.apis:
                result['Apis'].append(k.to_map() if k else None)
        if self.product is not None:
            result['Product'] = self.product
        if self.product_desc is not None:
            result['ProductDesc'] = self.product_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apis = []
        if m.get('Apis') is not None:
            for k in m.get('Apis'):
                temp_model = AiStoreUserTask()
                self.apis.append(temp_model.from_map(k))
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ProductDesc') is not None:
            self.product_desc = m.get('ProductDesc')
        return self


class AiStoreReceiveConfigDingTalk(TeaModel):
    def __init__(
        self,
        address: str = None,
        secret: str = None,
    ):
        self.address = address
        self.secret = secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.secret is not None:
            result['Secret'] = self.secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        return self


class AiStoreReceiveConfigEventBridge(TeaModel):
    def __init__(
        self,
        event_bus: str = None,
        event_rule: str = None,
    ):
        self.event_bus = event_bus
        self.event_rule = event_rule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bus is not None:
            result['EventBus'] = self.event_bus
        if self.event_rule is not None:
            result['EventRule'] = self.event_rule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBus') is not None:
            self.event_bus = m.get('EventBus')
        if m.get('EventRule') is not None:
            self.event_rule = m.get('EventRule')
        return self


class AiStoreReceiveConfigHttp(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class AiStoreReceiveConfigHttps(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class AiStoreReceiveConfigMns(TeaModel):
    def __init__(
        self,
        queue: str = None,
    ):
        self.queue = queue

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue is not None:
            result['Queue'] = self.queue
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        return self


class AiStoreReceiveConfigRocketMQ(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        topic_name: str = None,
    ):
        self.instance_id = instance_id
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class AiStoreReceiveConfig(TeaModel):
    def __init__(
        self,
        custom: str = None,
        ding_talk: AiStoreReceiveConfigDingTalk = None,
        event_bridge: AiStoreReceiveConfigEventBridge = None,
        http: AiStoreReceiveConfigHttp = None,
        https: AiStoreReceiveConfigHttps = None,
        mns: AiStoreReceiveConfigMns = None,
        rocket_mq: AiStoreReceiveConfigRocketMQ = None,
    ):
        self.custom = custom
        self.ding_talk = ding_talk
        self.event_bridge = event_bridge
        self.http = http
        self.https = https
        self.mns = mns
        self.rocket_mq = rocket_mq

    def validate(self):
        if self.ding_talk:
            self.ding_talk.validate()
        if self.event_bridge:
            self.event_bridge.validate()
        if self.http:
            self.http.validate()
        if self.https:
            self.https.validate()
        if self.mns:
            self.mns.validate()
        if self.rocket_mq:
            self.rocket_mq.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom is not None:
            result['Custom'] = self.custom
        if self.ding_talk is not None:
            result['DingTalk'] = self.ding_talk.to_map()
        if self.event_bridge is not None:
            result['EventBridge'] = self.event_bridge.to_map()
        if self.http is not None:
            result['Http'] = self.http.to_map()
        if self.https is not None:
            result['Https'] = self.https.to_map()
        if self.mns is not None:
            result['Mns'] = self.mns.to_map()
        if self.rocket_mq is not None:
            result['RocketMQ'] = self.rocket_mq.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Custom') is not None:
            self.custom = m.get('Custom')
        if m.get('DingTalk') is not None:
            temp_model = AiStoreReceiveConfigDingTalk()
            self.ding_talk = temp_model.from_map(m['DingTalk'])
        if m.get('EventBridge') is not None:
            temp_model = AiStoreReceiveConfigEventBridge()
            self.event_bridge = temp_model.from_map(m['EventBridge'])
        if m.get('Http') is not None:
            temp_model = AiStoreReceiveConfigHttp()
            self.http = temp_model.from_map(m['Http'])
        if m.get('Https') is not None:
            temp_model = AiStoreReceiveConfigHttps()
            self.https = temp_model.from_map(m['Https'])
        if m.get('Mns') is not None:
            temp_model = AiStoreReceiveConfigMns()
            self.mns = temp_model.from_map(m['Mns'])
        if m.get('RocketMQ') is not None:
            temp_model = AiStoreReceiveConfigRocketMQ()
            self.rocket_mq = temp_model.from_map(m['RocketMQ'])
        return self


class AiStoreTemplate(TeaModel):
    def __init__(
        self,
        template_context: str = None,
        template_variable: str = None,
    ):
        self.template_context = template_context
        self.template_variable = template_variable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_context is not None:
            result['TemplateContext'] = self.template_context
        if self.template_variable is not None:
            result['TemplateVariable'] = self.template_variable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateContext') is not None:
            self.template_context = m.get('TemplateContext')
        if m.get('TemplateVariable') is not None:
            self.template_variable = m.get('TemplateVariable')
        return self


class CheckServiceLinkedRoleForDeletingRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        deletion_task_id: str = None,
        role_arn: str = None,
        spiregion_id: str = None,
        service_name: str = None,
    ):
        self.account_id = account_id
        self.deletion_task_id = deletion_task_id
        self.role_arn = role_arn
        self.spiregion_id = spiregion_id
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.spiregion_id is not None:
            result['SPIRegionId'] = self.spiregion_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('SPIRegionId') is not None:
            self.spiregion_id = m.get('SPIRegionId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages(TeaModel):
    def __init__(
        self,
        region: str = None,
        resources: List[bytes] = None,
    ):
        self.region = region
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class CheckServiceLinkedRoleForDeletingResponseBody(TeaModel):
    def __init__(
        self,
        deletable: bool = None,
        request_id: str = None,
        role_usages: List[CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages] = None,
    ):
        self.deletable = deletable
        self.request_id = request_id
        self.role_usages = role_usages

    def validate(self):
        if self.role_usages:
            for k in self.role_usages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deletable is not None:
            result['Deletable'] = self.deletable
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RoleUsages'] = []
        if self.role_usages is not None:
            for k in self.role_usages:
                result['RoleUsages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.role_usages = []
        if m.get('RoleUsages') is not None:
            for k in m.get('RoleUsages'):
                temp_model = CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages()
                self.role_usages.append(temp_model.from_map(k))
        return self


class CheckServiceLinkedRoleForDeletingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckServiceLinkedRoleForDeletingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckServiceLinkedRoleForDeletingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAiStoreBucketRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
    ):
        self.bucket_name = bucket_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        return self


class CreateAiStoreBucketResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAiStoreBucketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAiStoreBucketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAiStoreBucketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAiStoreReceiveConfigRequest(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        product: str = None,
    ):
        self.api_name = api_name
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class CreateAiStoreReceiveConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: AiStoreReceiveConfig = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = AiStoreReceiveConfig()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAiStoreReceiveConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAiStoreReceiveConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAiStoreReceiveConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAiStoreUserTaskRequest(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        bucket_key_prefix: str = None,
        bucket_name: str = None,
        create_config: str = None,
        name: str = None,
        param_info: str = None,
        product: str = None,
        receive_config: str = None,
        remark: str = None,
        status: str = None,
    ):
        self.api_name = api_name
        self.bucket_key_prefix = bucket_key_prefix
        self.bucket_name = bucket_name
        self.create_config = create_config
        self.name = name
        self.param_info = param_info
        self.product = product
        self.receive_config = receive_config
        self.remark = remark
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.bucket_key_prefix is not None:
            result['BucketKeyPrefix'] = self.bucket_key_prefix
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.create_config is not None:
            result['CreateConfig'] = self.create_config
        if self.name is not None:
            result['Name'] = self.name
        if self.param_info is not None:
            result['ParamInfo'] = self.param_info
        if self.product is not None:
            result['Product'] = self.product
        if self.receive_config is not None:
            result['ReceiveConfig'] = self.receive_config
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BucketKeyPrefix') is not None:
            self.bucket_key_prefix = m.get('BucketKeyPrefix')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CreateConfig') is not None:
            self.create_config = m.get('CreateConfig')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamInfo') is not None:
            self.param_info = m.get('ParamInfo')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ReceiveConfig') is not None:
            self.receive_config = m.get('ReceiveConfig')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateAiStoreUserTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAiStoreUserTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAiStoreUserTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAiStoreUserTaskRequest(TeaModel):
    def __init__(
        self,
        aistore_version: str = None,
        id: int = None,
    ):
        self.aistore_version = aistore_version
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aistore_version is not None:
            result['AistoreVersion'] = self.aistore_version
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AistoreVersion') is not None:
            self.aistore_version = m.get('AistoreVersion')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteAiStoreUserTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAiStoreUserTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAiStoreUserTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAiStoreUserTaskRequest(TeaModel):
    def __init__(
        self,
        aistore_version: str = None,
        id: int = None,
    ):
        self.aistore_version = aistore_version
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aistore_version is not None:
            result['AistoreVersion'] = self.aistore_version
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AistoreVersion') is not None:
            self.aistore_version = m.get('AistoreVersion')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DisableAiStoreUserTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableAiStoreUserTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableAiStoreUserTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAiStoreUserTaskRequest(TeaModel):
    def __init__(
        self,
        aistore_version: str = None,
        id: int = None,
    ):
        self.aistore_version = aistore_version
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aistore_version is not None:
            result['AistoreVersion'] = self.aistore_version
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AistoreVersion') is not None:
            self.aistore_version = m.get('AistoreVersion')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class EnableAiStoreUserTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableAiStoreUserTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableAiStoreUserTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAiStoreReceiveConfigRequest(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        product: str = None,
    ):
        self.api_name = api_name
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class GetAiStoreReceiveConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: AiStoreReceiveConfig = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = AiStoreReceiveConfig()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAiStoreReceiveConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAiStoreReceiveConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAiStoreReceiveConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAiStoreUserTaskRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetAiStoreUserTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: AiStoreUserTask = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = AiStoreUserTask()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAiStoreUserTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAiStoreUserTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAiStoreUserTaskByNameRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetAiStoreUserTaskByNameResponseBody(TeaModel):
    def __init__(
        self,
        data: AiStoreUserTask = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = AiStoreUserTask()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAiStoreUserTaskByNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAiStoreUserTaskByNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAiStoreUserTaskByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAiStoreBucketsRequest(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        product: str = None,
    ):
        self.api_name = api_name
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class ListAiStoreBucketsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[str] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAiStoreBucketsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAiStoreBucketsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAiStoreBucketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAiStoreApiTreeResponseBody(TeaModel):
    def __init__(
        self,
        data: List[AiStoreApiNode] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AiStoreApiNode()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryAiStoreApiTreeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAiStoreApiTreeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryAiStoreApiTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAiStoreRegionsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[AiStoreUserTask] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AiStoreUserTask()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryAiStoreRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAiStoreRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryAiStoreRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAiStoreUserTaskPageRequest(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        bucket_name: str = None,
        name: str = None,
        page_no: int = None,
        page_size: int = None,
        product: str = None,
        status: str = None,
    ):
        self.api_name = api_name
        self.bucket_name = bucket_name
        self.name = name
        self.page_no = page_no
        self.page_size = page_size
        self.product = product
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.name is not None:
            result['Name'] = self.name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product is not None:
            result['Product'] = self.product
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryAiStoreUserTaskPageResponseBodyData(TeaModel):
    def __init__(
        self,
        task_list: List[AiStoreUserTask] = None,
        total_count: int = None,
    ):
        self.task_list = task_list
        self.total_count = total_count

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = AiStoreUserTask()
                self.task_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryAiStoreUserTaskPageResponseBody(TeaModel):
    def __init__(
        self,
        data: QueryAiStoreUserTaskPageResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryAiStoreUserTaskPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryAiStoreUserTaskPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAiStoreUserTaskPageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryAiStoreUserTaskPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAiStoreUserTaskRequest(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        bucket_key_prefix: str = None,
        bucket_name: str = None,
        id: int = None,
        name: str = None,
        param_info: str = None,
        product: str = None,
        receive_config: str = None,
        remark: str = None,
        status: str = None,
    ):
        self.api_name = api_name
        self.bucket_key_prefix = bucket_key_prefix
        self.bucket_name = bucket_name
        self.id = id
        self.name = name
        self.param_info = param_info
        self.product = product
        self.receive_config = receive_config
        self.remark = remark
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.bucket_key_prefix is not None:
            result['BucketKeyPrefix'] = self.bucket_key_prefix
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.param_info is not None:
            result['ParamInfo'] = self.param_info
        if self.product is not None:
            result['Product'] = self.product
        if self.receive_config is not None:
            result['ReceiveConfig'] = self.receive_config
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BucketKeyPrefix') is not None:
            self.bucket_key_prefix = m.get('BucketKeyPrefix')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamInfo') is not None:
            self.param_info = m.get('ParamInfo')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ReceiveConfig') is not None:
            self.receive_config = m.get('ReceiveConfig')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateAiStoreUserTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAiStoreUserTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAiStoreUserTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


