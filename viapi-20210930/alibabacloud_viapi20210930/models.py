# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AiStoreUserTask(TeaModel):
    def __init__(
        self,
        id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        region: str = None,
        region_desc: str = None,
        name: str = None,
        product: str = None,
        product_desc: str = None,
        api_name: str = None,
        api_desc: str = None,
        version: str = None,
        param_info: str = None,
        bucket_name: str = None,
        bucket_key_prefix: str = None,
        remark: str = None,
        receive_config: str = None,
        status: str = None,
        enable_time: str = None,
        disable_time: str = None,
    ):
        # ID
        self.id = id
        # 创建时间
        self.gmt_create = gmt_create
        # 修改时间
        self.gmt_modified = gmt_modified
        # 地域
        self.region = region
        # 地域描述
        self.region_desc = region_desc
        # 任务名称
        self.name = name
        # 产品名称
        self.product = product
        # 产品描述
        self.product_desc = product_desc
        # API名称
        self.api_name = api_name
        # API描述
        self.api_desc = api_desc
        # API版本
        self.version = version
        # 参数信息
        self.param_info = param_info
        # bucket名称
        self.bucket_name = bucket_name
        # bucketKey前缀
        self.bucket_key_prefix = bucket_key_prefix
        # 备注
        self.remark = remark
        # 接收消息配置
        self.receive_config = receive_config
        # 状态
        self.status = status
        # 启用时间
        self.enable_time = enable_time
        # 停用时间
        self.disable_time = disable_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.region is not None:
            result['Region'] = self.region
        if self.region_desc is not None:
            result['RegionDesc'] = self.region_desc
        if self.name is not None:
            result['Name'] = self.name
        if self.product is not None:
            result['Product'] = self.product
        if self.product_desc is not None:
            result['ProductDesc'] = self.product_desc
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.api_desc is not None:
            result['ApiDesc'] = self.api_desc
        if self.version is not None:
            result['Version'] = self.version
        if self.param_info is not None:
            result['ParamInfo'] = self.param_info
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.bucket_key_prefix is not None:
            result['BucketKeyPrefix'] = self.bucket_key_prefix
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.receive_config is not None:
            result['ReceiveConfig'] = self.receive_config
        if self.status is not None:
            result['Status'] = self.status
        if self.enable_time is not None:
            result['EnableTime'] = self.enable_time
        if self.disable_time is not None:
            result['DisableTime'] = self.disable_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionDesc') is not None:
            self.region_desc = m.get('RegionDesc')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ProductDesc') is not None:
            self.product_desc = m.get('ProductDesc')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('ApiDesc') is not None:
            self.api_desc = m.get('ApiDesc')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ParamInfo') is not None:
            self.param_info = m.get('ParamInfo')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('BucketKeyPrefix') is not None:
            self.bucket_key_prefix = m.get('BucketKeyPrefix')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ReceiveConfig') is not None:
            self.receive_config = m.get('ReceiveConfig')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('EnableTime') is not None:
            self.enable_time = m.get('EnableTime')
        if m.get('DisableTime') is not None:
            self.disable_time = m.get('DisableTime')
        return self


class AiStoreReceiveConfigEventBridge(TeaModel):
    def __init__(
        self,
        event_bus: str = None,
        event_rule: str = None,
    ):
        # 事件总线
        self.event_bus = event_bus
        # 事件规则
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


class AiStoreReceiveConfigMns(TeaModel):
    def __init__(
        self,
        queue: str = None,
    ):
        # 消息队列
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


class AiStoreReceiveConfig(TeaModel):
    def __init__(
        self,
        event_bridge: AiStoreReceiveConfigEventBridge = None,
        mns: AiStoreReceiveConfigMns = None,
    ):
        # 事件总线
        self.event_bridge = event_bridge
        # MNS消息
        self.mns = mns

    def validate(self):
        if self.event_bridge:
            self.event_bridge.validate()
        if self.mns:
            self.mns.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_bridge is not None:
            result['EventBridge'] = self.event_bridge.to_map()
        if self.mns is not None:
            result['Mns'] = self.mns.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBridge') is not None:
            temp_model = AiStoreReceiveConfigEventBridge()
            self.event_bridge = temp_model.from_map(m['EventBridge'])
        if m.get('Mns') is not None:
            temp_model = AiStoreReceiveConfigMns()
            self.mns = temp_model.from_map(m['Mns'])
        return self


class AiStoreApiNode(TeaModel):
    def __init__(
        self,
        product: str = None,
        product_desc: str = None,
        apis: List[AiStoreUserTask] = None,
    ):
        # 产品名称
        self.product = product
        # 产品描述
        self.product_desc = product_desc
        # API列表
        self.apis = apis

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
        if self.product is not None:
            result['Product'] = self.product
        if self.product_desc is not None:
            result['ProductDesc'] = self.product_desc
        result['Apis'] = []
        if self.apis is not None:
            for k in self.apis:
                result['Apis'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ProductDesc') is not None:
            self.product_desc = m.get('ProductDesc')
        self.apis = []
        if m.get('Apis') is not None:
            for k in m.get('Apis'):
                temp_model = AiStoreUserTask()
                self.apis.append(temp_model.from_map(k))
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
        request_id: str = None,
        data: AiStoreUserTask = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AiStoreUserTask()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAiStoreUserTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAiStoreUserTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAiStoreUserTaskPageRequest(TeaModel):
    def __init__(
        self,
        product: str = None,
        api_name: str = None,
        status: str = None,
        page_no: int = None,
        page_size: int = None,
        name: str = None,
        bucket_name: str = None,
    ):
        self.product = product
        self.api_name = api_name
        self.status = status
        self.page_no = page_no
        self.page_size = page_size
        self.name = name
        self.bucket_name = bucket_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.status is not None:
            result['Status'] = self.status
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.name is not None:
            result['Name'] = self.name
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
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
        request_id: str = None,
        data: QueryAiStoreUserTaskPageResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryAiStoreUserTaskPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryAiStoreUserTaskPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAiStoreUserTaskPageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryAiStoreUserTaskPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAiStoreRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[AiStoreUserTask] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AiStoreUserTask()
                self.data.append(temp_model.from_map(k))
        return self


class QueryAiStoreRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAiStoreRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryAiStoreRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAiStoreBucketsRequest(TeaModel):
    def __init__(
        self,
        product: str = None,
        api_name: str = None,
    ):
        self.product = product
        self.api_name = api_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        return self


class ListAiStoreBucketsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[str] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ListAiStoreBucketsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAiStoreBucketsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAiStoreBucketsResponseBody()
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
        request_id: str = None,
        data: AiStoreUserTask = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AiStoreUserTask()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAiStoreUserTaskByNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAiStoreUserTaskByNameResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAiStoreUserTaskByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAiStoreUserTaskRequest(TeaModel):
    def __init__(
        self,
        product: str = None,
        api_name: str = None,
        bucket_name: str = None,
        bucket_key_prefix: str = None,
        name: str = None,
        param_info: str = None,
        remark: str = None,
        receive_config: str = None,
        status: str = None,
        id: int = None,
    ):
        self.product = product
        self.api_name = api_name
        self.bucket_name = bucket_name
        self.bucket_key_prefix = bucket_key_prefix
        self.name = name
        self.param_info = param_info
        self.remark = remark
        self.receive_config = receive_config
        self.status = status
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.bucket_key_prefix is not None:
            result['BucketKeyPrefix'] = self.bucket_key_prefix
        if self.name is not None:
            result['Name'] = self.name
        if self.param_info is not None:
            result['ParamInfo'] = self.param_info
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.receive_config is not None:
            result['ReceiveConfig'] = self.receive_config
        if self.status is not None:
            result['Status'] = self.status
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('BucketKeyPrefix') is not None:
            self.bucket_key_prefix = m.get('BucketKeyPrefix')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamInfo') is not None:
            self.param_info = m.get('ParamInfo')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ReceiveConfig') is not None:
            self.receive_config = m.get('ReceiveConfig')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateAiStoreUserTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class UpdateAiStoreUserTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAiStoreUserTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAiStoreUserTaskRequest(TeaModel):
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


class DisableAiStoreUserTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class DisableAiStoreUserTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableAiStoreUserTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAiStoreApiTreeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[AiStoreApiNode] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AiStoreApiNode()
                self.data.append(temp_model.from_map(k))
        return self


class QueryAiStoreApiTreeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAiStoreApiTreeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryAiStoreApiTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAiStoreUserTaskRequest(TeaModel):
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


class DeleteAiStoreUserTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class DeleteAiStoreUserTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAiStoreUserTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAiStoreUserTaskRequest(TeaModel):
    def __init__(
        self,
        product: str = None,
        api_name: str = None,
        bucket_name: str = None,
        bucket_key_prefix: str = None,
        name: str = None,
        param_info: str = None,
        remark: str = None,
        receive_config: str = None,
        status: str = None,
    ):
        self.product = product
        self.api_name = api_name
        self.bucket_name = bucket_name
        self.bucket_key_prefix = bucket_key_prefix
        self.name = name
        self.param_info = param_info
        self.remark = remark
        self.receive_config = receive_config
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.bucket_key_prefix is not None:
            result['BucketKeyPrefix'] = self.bucket_key_prefix
        if self.name is not None:
            result['Name'] = self.name
        if self.param_info is not None:
            result['ParamInfo'] = self.param_info
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.receive_config is not None:
            result['ReceiveConfig'] = self.receive_config
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('BucketKeyPrefix') is not None:
            self.bucket_key_prefix = m.get('BucketKeyPrefix')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParamInfo') is not None:
            self.param_info = m.get('ParamInfo')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ReceiveConfig') is not None:
            self.receive_config = m.get('ReceiveConfig')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateAiStoreUserTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class CreateAiStoreUserTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAiStoreUserTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAiStoreUserTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAiStoreReceiveConfigRequest(TeaModel):
    def __init__(
        self,
        product: str = None,
        api_name: str = None,
    ):
        self.product = product
        self.api_name = api_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        return self


class CreateAiStoreReceiveConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AiStoreReceiveConfig = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AiStoreReceiveConfig()
            self.data = temp_model.from_map(m['Data'])
        return self


class CreateAiStoreReceiveConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAiStoreReceiveConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAiStoreReceiveConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAiStoreReceiveConfigRequest(TeaModel):
    def __init__(
        self,
        product: str = None,
        api_name: str = None,
    ):
        self.product = product
        self.api_name = api_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product is not None:
            result['Product'] = self.product
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        return self


class GetAiStoreReceiveConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AiStoreReceiveConfig = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AiStoreReceiveConfig()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAiStoreReceiveConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAiStoreReceiveConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAiStoreReceiveConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAiStoreUserTaskRequest(TeaModel):
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


class EnableAiStoreUserTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class EnableAiStoreUserTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableAiStoreUserTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableAiStoreUserTaskResponseBody()
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
        request_id: str = None,
        data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class CreateAiStoreBucketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAiStoreBucketResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAiStoreBucketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckServiceLinkedRoleForDeletingRequest(TeaModel):
    def __init__(
        self,
        role_arn: str = None,
        service_name: str = None,
        spiregion_id: str = None,
        deletion_task_id: str = None,
        account_id: str = None,
    ):
        self.role_arn = role_arn
        self.service_name = service_name
        self.spiregion_id = spiregion_id
        self.deletion_task_id = deletion_task_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.spiregion_id is not None:
            result['SPIRegionId'] = self.spiregion_id
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SPIRegionId') is not None:
            self.spiregion_id = m.get('SPIRegionId')
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
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
        request_id: str = None,
        deletable: bool = None,
        role_usages: List[CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.deletable = deletable
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.deletable is not None:
            result['Deletable'] = self.deletable
        result['RoleUsages'] = []
        if self.role_usages is not None:
            for k in self.role_usages:
                result['RoleUsages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')
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
        body: CheckServiceLinkedRoleForDeletingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckServiceLinkedRoleForDeletingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


