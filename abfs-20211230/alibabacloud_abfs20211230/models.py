# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class CreateBackFlowRequest(TeaModel):
    def __init__(
        self,
        odps_partition: str = None,
        timestamp: str = None,
    ):
        self.odps_partition = odps_partition
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.odps_partition is not None:
            result['odpsPartition'] = self.odps_partition
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('odpsPartition') is not None:
            self.odps_partition = m.get('odpsPartition')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class CreateBackFlowResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # 错误码
        self.code = code
        # 错误消息
        self.message = message
        # Id of the request
        self.request_id = request_id
        # result
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateBackFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateBackFlowResponseBody = None,
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
            temp_model = CreateBackFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceTableRequestFieldMapFields(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        is_multi_value: bool = None,
        is_virtual: bool = None,
        online_status: bool = None,
        pkey: bool = None,
        plugin_name: str = None,
        plugin_param: str = None,
        seperator: str = None,
        source_name: str = None,
        source_type: str = None,
        target_name: str = None,
        target_type: str = None,
    ):
        # 默认值
        self.default_value = default_value
        # 描述
        self.description = description
        self.is_multi_value = is_multi_value
        self.is_virtual = is_virtual
        self.online_status = online_status
        # 是否为主键
        self.pkey = pkey
        # 插件名
        self.plugin_name = plugin_name
        # 插件信息
        self.plugin_param = plugin_param
        # 分隔符
        self.seperator = seperator
        # 源字段名
        self.source_name = source_name
        # 源字段类型
        self.source_type = source_type
        # 目标字段名
        self.target_name = target_name
        # 目标字段类型
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.description is not None:
            result['description'] = self.description
        if self.is_multi_value is not None:
            result['isMultiValue'] = self.is_multi_value
        if self.is_virtual is not None:
            result['isVirtual'] = self.is_virtual
        if self.online_status is not None:
            result['onlineStatus'] = self.online_status
        if self.pkey is not None:
            result['pkey'] = self.pkey
        if self.plugin_name is not None:
            result['pluginName'] = self.plugin_name
        if self.plugin_param is not None:
            result['pluginParam'] = self.plugin_param
        if self.seperator is not None:
            result['seperator'] = self.seperator
        if self.source_name is not None:
            result['sourceName'] = self.source_name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.target_name is not None:
            result['targetName'] = self.target_name
        if self.target_type is not None:
            result['targetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('isMultiValue') is not None:
            self.is_multi_value = m.get('isMultiValue')
        if m.get('isVirtual') is not None:
            self.is_virtual = m.get('isVirtual')
        if m.get('onlineStatus') is not None:
            self.online_status = m.get('onlineStatus')
        if m.get('pkey') is not None:
            self.pkey = m.get('pkey')
        if m.get('pluginName') is not None:
            self.plugin_name = m.get('pluginName')
        if m.get('pluginParam') is not None:
            self.plugin_param = m.get('pluginParam')
        if m.get('seperator') is not None:
            self.seperator = m.get('seperator')
        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('targetName') is not None:
            self.target_name = m.get('targetName')
        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')
        return self


class CreateInstanceTableRequestFieldMapIndexs(TeaModel):
    def __init__(
        self,
        field: str = None,
        index_name: str = None,
    ):
        # 字段名
        self.field = field
        # 索引字段名
        self.index_name = index_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['field'] = self.field
        if self.index_name is not None:
            result['indexName'] = self.index_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('field') is not None:
            self.field = m.get('field')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        return self


class CreateInstanceTableRequestFieldMap(TeaModel):
    def __init__(
        self,
        fields: List[CreateInstanceTableRequestFieldMapFields] = None,
        indexs: List[CreateInstanceTableRequestFieldMapIndexs] = None,
        is_attribute_pack: bool = None,
        max_skey_num: int = None,
        offline_build_protection_threshold: int = None,
        pkey: str = None,
        record_type: str = None,
    ):
        self.fields = fields
        # 索引信息
        self.indexs = indexs
        self.is_attribute_pack = is_attribute_pack
        # 最大外建数
        self.max_skey_num = max_skey_num
        # 离线构建线程数
        self.offline_build_protection_threshold = offline_build_protection_threshold
        # 主键
        self.pkey = pkey
        # 记录类型
        self.record_type = record_type

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()
        if self.indexs:
            for k in self.indexs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['fields'].append(k.to_map() if k else None)
        result['indexs'] = []
        if self.indexs is not None:
            for k in self.indexs:
                result['indexs'].append(k.to_map() if k else None)
        if self.is_attribute_pack is not None:
            result['isAttributePack'] = self.is_attribute_pack
        if self.max_skey_num is not None:
            result['maxSkeyNum'] = self.max_skey_num
        if self.offline_build_protection_threshold is not None:
            result['offlineBuildProtectionThreshold'] = self.offline_build_protection_threshold
        if self.pkey is not None:
            result['pkey'] = self.pkey
        if self.record_type is not None:
            result['recordType'] = self.record_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('fields') is not None:
            for k in m.get('fields'):
                temp_model = CreateInstanceTableRequestFieldMapFields()
                self.fields.append(temp_model.from_map(k))
        self.indexs = []
        if m.get('indexs') is not None:
            for k in m.get('indexs'):
                temp_model = CreateInstanceTableRequestFieldMapIndexs()
                self.indexs.append(temp_model.from_map(k))
        if m.get('isAttributePack') is not None:
            self.is_attribute_pack = m.get('isAttributePack')
        if m.get('maxSkeyNum') is not None:
            self.max_skey_num = m.get('maxSkeyNum')
        if m.get('offlineBuildProtectionThreshold') is not None:
            self.offline_build_protection_threshold = m.get('offlineBuildProtectionThreshold')
        if m.get('pkey') is not None:
            self.pkey = m.get('pkey')
        if m.get('recordType') is not None:
            self.record_type = m.get('recordType')
        return self


class CreateInstanceTableRequestFullDataSourceConfigOdpsDataDesc(TeaModel):
    def __init__(
        self,
        project: str = None,
        table: str = None,
    ):
        # 项目名
        self.project = project
        # 表名
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class CreateInstanceTableRequestFullDataSourceConfig(TeaModel):
    def __init__(
        self,
        odps_data_desc: CreateInstanceTableRequestFullDataSourceConfigOdpsDataDesc = None,
        type: str = None,
    ):
        # MaxCompute描述
        self.odps_data_desc = odps_data_desc
        # 数据源类型
        self.type = type

    def validate(self):
        if self.odps_data_desc:
            self.odps_data_desc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.odps_data_desc is not None:
            result['odpsDataDesc'] = self.odps_data_desc.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('odpsDataDesc') is not None:
            temp_model = CreateInstanceTableRequestFullDataSourceConfigOdpsDataDesc()
            self.odps_data_desc = temp_model.from_map(m['odpsDataDesc'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateInstanceTableRequestIncDataSourceConfigSwiftDataDesc(TeaModel):
    def __init__(
        self,
        topic: str = None,
    ):
        # topic
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.topic is not None:
            result['topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        return self


class CreateInstanceTableRequestIncDataSourceConfig(TeaModel):
    def __init__(
        self,
        swift_data_desc: CreateInstanceTableRequestIncDataSourceConfigSwiftDataDesc = None,
        type: str = None,
    ):
        self.swift_data_desc = swift_data_desc
        # 数据源类型
        self.type = type

    def validate(self):
        if self.swift_data_desc:
            self.swift_data_desc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.swift_data_desc is not None:
            result['swiftDataDesc'] = self.swift_data_desc.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('swiftDataDesc') is not None:
            temp_model = CreateInstanceTableRequestIncDataSourceConfigSwiftDataDesc()
            self.swift_data_desc = temp_model.from_map(m['swiftDataDesc'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateInstanceTableRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        field_map: CreateInstanceTableRequestFieldMap = None,
        full_data_source_config: CreateInstanceTableRequestFullDataSourceConfig = None,
        inc_data_source_config: CreateInstanceTableRequestIncDataSourceConfig = None,
        index_type: str = None,
        table_name: str = None,
        trigger_mode: str = None,
        ttl: int = None,
    ):
        # 描述
        self.description = description
        # 字段描述
        self.field_map = field_map
        # 全量数据源描述
        self.full_data_source_config = full_data_source_config
        # 增量数据源描述
        self.inc_data_source_config = inc_data_source_config
        # 索引类型
        self.index_type = index_type
        # 表名
        self.table_name = table_name
        # 回流触发模式
        self.trigger_mode = trigger_mode
        # Topic过期时间
        self.ttl = ttl

    def validate(self):
        if self.field_map:
            self.field_map.validate()
        if self.full_data_source_config:
            self.full_data_source_config.validate()
        if self.inc_data_source_config:
            self.inc_data_source_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.field_map is not None:
            result['fieldMap'] = self.field_map.to_map()
        if self.full_data_source_config is not None:
            result['fullDataSourceConfig'] = self.full_data_source_config.to_map()
        if self.inc_data_source_config is not None:
            result['incDataSourceConfig'] = self.inc_data_source_config.to_map()
        if self.index_type is not None:
            result['indexType'] = self.index_type
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.trigger_mode is not None:
            result['triggerMode'] = self.trigger_mode
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('fieldMap') is not None:
            temp_model = CreateInstanceTableRequestFieldMap()
            self.field_map = temp_model.from_map(m['fieldMap'])
        if m.get('fullDataSourceConfig') is not None:
            temp_model = CreateInstanceTableRequestFullDataSourceConfig()
            self.full_data_source_config = temp_model.from_map(m['fullDataSourceConfig'])
        if m.get('incDataSourceConfig') is not None:
            temp_model = CreateInstanceTableRequestIncDataSourceConfig()
            self.inc_data_source_config = temp_model.from_map(m['incDataSourceConfig'])
        if m.get('indexType') is not None:
            self.index_type = m.get('indexType')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('triggerMode') is not None:
            self.trigger_mode = m.get('triggerMode')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class CreateInstanceTableResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # 错误码
        self.code = code
        # 消息
        self.message = message
        # Id of the request
        self.request_id = request_id
        # result
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class CreateInstanceTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInstanceTableResponseBody = None,
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
            temp_model = CreateInstanceTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceTableResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # 错误码
        self.code = code
        # 错误信息
        self.message = message
        # Id of the request
        self.request_id = request_id
        # reuslt
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteInstanceTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInstanceTableResponseBody = None,
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
            temp_model = DeleteInstanceTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBackFlowResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # code
        self.code = code
        # error message
        self.message = message
        # Id of the request
        self.request_id = request_id
        # result
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class GetBackFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBackFlowResponseBody = None,
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
            temp_model = GetBackFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIndexesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # code
        self.code = code
        # error message
        self.message = message
        # Id of the request
        self.request_id = request_id
        # result
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class GetIndexesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetIndexesResponseBody = None,
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
            temp_model = GetIndexesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # 状态码
        self.code = code
        # 消息
        self.message = message
        # 请求ID
        self.request_id = request_id
        # 结果
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceResponseBody = None,
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
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceTableResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class GetInstanceTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceTableResponseBody = None,
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
            temp_model = GetInstanceTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBackFlowsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
    ):
        # 查询回流次数(默认值为1,最大值为10)
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        return self


class ListBackFlowsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[Dict[str, Any]] = None,
    ):
        # code
        self.code = code
        # error message
        self.message = message
        # Id of the request
        self.request_id = request_id
        # result
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListBackFlowsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBackFlowsResponseBody = None,
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
            temp_model = ListBackFlowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceTableRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # 起始页
        self.page_number = page_number
        # 页码大小
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListInstanceTableResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListInstanceTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstanceTableResponseBody = None,
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
            temp_model = ListInstanceTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # 起始页
        self.page_number = page_number
        # 页码大小
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # 错误码
        self.code = code
        # 消息
        self.message = message
        # 请求ID
        self.request_id = request_id
        # 结果数据
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstancesResponseBody = None,
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
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceTableRequestFieldMapFields(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        is_multi_value: bool = None,
        is_virtual: bool = None,
        online_status: bool = None,
        pkey: bool = None,
        plugin_name: str = None,
        plugin_param: str = None,
        seperator: str = None,
        source_name: str = None,
        source_type: str = None,
        target_name: str = None,
        target_type: str = None,
    ):
        # 默认值
        self.default_value = default_value
        # 描述
        self.description = description
        self.is_multi_value = is_multi_value
        self.is_virtual = is_virtual
        self.online_status = online_status
        # 是否为主键
        self.pkey = pkey
        # 插件名
        self.plugin_name = plugin_name
        # 插件信息
        self.plugin_param = plugin_param
        # 分隔符
        self.seperator = seperator
        # 源字段名
        self.source_name = source_name
        # 源字段类型
        self.source_type = source_type
        # 目标字段名
        self.target_name = target_name
        # 目标字段类型
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.description is not None:
            result['description'] = self.description
        if self.is_multi_value is not None:
            result['isMultiValue'] = self.is_multi_value
        if self.is_virtual is not None:
            result['isVirtual'] = self.is_virtual
        if self.online_status is not None:
            result['onlineStatus'] = self.online_status
        if self.pkey is not None:
            result['pkey'] = self.pkey
        if self.plugin_name is not None:
            result['pluginName'] = self.plugin_name
        if self.plugin_param is not None:
            result['pluginParam'] = self.plugin_param
        if self.seperator is not None:
            result['seperator'] = self.seperator
        if self.source_name is not None:
            result['sourceName'] = self.source_name
        if self.source_type is not None:
            result['sourceType'] = self.source_type
        if self.target_name is not None:
            result['targetName'] = self.target_name
        if self.target_type is not None:
            result['targetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('isMultiValue') is not None:
            self.is_multi_value = m.get('isMultiValue')
        if m.get('isVirtual') is not None:
            self.is_virtual = m.get('isVirtual')
        if m.get('onlineStatus') is not None:
            self.online_status = m.get('onlineStatus')
        if m.get('pkey') is not None:
            self.pkey = m.get('pkey')
        if m.get('pluginName') is not None:
            self.plugin_name = m.get('pluginName')
        if m.get('pluginParam') is not None:
            self.plugin_param = m.get('pluginParam')
        if m.get('seperator') is not None:
            self.seperator = m.get('seperator')
        if m.get('sourceName') is not None:
            self.source_name = m.get('sourceName')
        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')
        if m.get('targetName') is not None:
            self.target_name = m.get('targetName')
        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')
        return self


class UpdateInstanceTableRequestFieldMapIndexs(TeaModel):
    def __init__(
        self,
        field: str = None,
        index_name: str = None,
    ):
        # 字段名
        self.field = field
        # 索引字段名
        self.index_name = index_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['field'] = self.field
        if self.index_name is not None:
            result['indexName'] = self.index_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('field') is not None:
            self.field = m.get('field')
        if m.get('indexName') is not None:
            self.index_name = m.get('indexName')
        return self


class UpdateInstanceTableRequestFieldMap(TeaModel):
    def __init__(
        self,
        fields: List[UpdateInstanceTableRequestFieldMapFields] = None,
        indexs: List[UpdateInstanceTableRequestFieldMapIndexs] = None,
        is_attribute_pack: bool = None,
        max_skey_num: int = None,
        offline_build_protection_threshold: int = None,
        pkey: str = None,
        record_type: str = None,
    ):
        self.fields = fields
        # 索引信息
        self.indexs = indexs
        self.is_attribute_pack = is_attribute_pack
        # 最大外建数
        self.max_skey_num = max_skey_num
        # 离线构建线程数
        self.offline_build_protection_threshold = offline_build_protection_threshold
        # 主键
        self.pkey = pkey
        # 记录类型
        self.record_type = record_type

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()
        if self.indexs:
            for k in self.indexs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['fields'].append(k.to_map() if k else None)
        result['indexs'] = []
        if self.indexs is not None:
            for k in self.indexs:
                result['indexs'].append(k.to_map() if k else None)
        if self.is_attribute_pack is not None:
            result['isAttributePack'] = self.is_attribute_pack
        if self.max_skey_num is not None:
            result['maxSkeyNum'] = self.max_skey_num
        if self.offline_build_protection_threshold is not None:
            result['offlineBuildProtectionThreshold'] = self.offline_build_protection_threshold
        if self.pkey is not None:
            result['pkey'] = self.pkey
        if self.record_type is not None:
            result['recordType'] = self.record_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('fields') is not None:
            for k in m.get('fields'):
                temp_model = UpdateInstanceTableRequestFieldMapFields()
                self.fields.append(temp_model.from_map(k))
        self.indexs = []
        if m.get('indexs') is not None:
            for k in m.get('indexs'):
                temp_model = UpdateInstanceTableRequestFieldMapIndexs()
                self.indexs.append(temp_model.from_map(k))
        if m.get('isAttributePack') is not None:
            self.is_attribute_pack = m.get('isAttributePack')
        if m.get('maxSkeyNum') is not None:
            self.max_skey_num = m.get('maxSkeyNum')
        if m.get('offlineBuildProtectionThreshold') is not None:
            self.offline_build_protection_threshold = m.get('offlineBuildProtectionThreshold')
        if m.get('pkey') is not None:
            self.pkey = m.get('pkey')
        if m.get('recordType') is not None:
            self.record_type = m.get('recordType')
        return self


class UpdateInstanceTableRequestFullDataSourceConfigOdpsDataDesc(TeaModel):
    def __init__(
        self,
        project: str = None,
        table: str = None,
    ):
        # 项目名
        self.project = project
        # 表名
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['project'] = self.project
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class UpdateInstanceTableRequestFullDataSourceConfig(TeaModel):
    def __init__(
        self,
        odps_data_desc: UpdateInstanceTableRequestFullDataSourceConfigOdpsDataDesc = None,
        type: str = None,
    ):
        # MaxCompute描述
        self.odps_data_desc = odps_data_desc
        # 数据源类型
        self.type = type

    def validate(self):
        if self.odps_data_desc:
            self.odps_data_desc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.odps_data_desc is not None:
            result['odpsDataDesc'] = self.odps_data_desc.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('odpsDataDesc') is not None:
            temp_model = UpdateInstanceTableRequestFullDataSourceConfigOdpsDataDesc()
            self.odps_data_desc = temp_model.from_map(m['odpsDataDesc'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateInstanceTableRequestIncDataSourceConfigSwiftDataDesc(TeaModel):
    def __init__(
        self,
        topic: str = None,
    ):
        # topic
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.topic is not None:
            result['topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('topic') is not None:
            self.topic = m.get('topic')
        return self


class UpdateInstanceTableRequestIncDataSourceConfig(TeaModel):
    def __init__(
        self,
        swift_data_desc: UpdateInstanceTableRequestIncDataSourceConfigSwiftDataDesc = None,
        type: str = None,
    ):
        self.swift_data_desc = swift_data_desc
        # 数据源类型
        self.type = type

    def validate(self):
        if self.swift_data_desc:
            self.swift_data_desc.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.swift_data_desc is not None:
            result['swiftDataDesc'] = self.swift_data_desc.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('swiftDataDesc') is not None:
            temp_model = UpdateInstanceTableRequestIncDataSourceConfigSwiftDataDesc()
            self.swift_data_desc = temp_model.from_map(m['swiftDataDesc'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UpdateInstanceTableRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        field_map: UpdateInstanceTableRequestFieldMap = None,
        full_data_source_config: UpdateInstanceTableRequestFullDataSourceConfig = None,
        inc_data_source_config: UpdateInstanceTableRequestIncDataSourceConfig = None,
        index_type: str = None,
        trigger_mode: str = None,
        ttl: int = None,
    ):
        # 描述
        self.description = description
        # 字段描述
        self.field_map = field_map
        # 全量数据源描述
        self.full_data_source_config = full_data_source_config
        # 增量数据源描述
        self.inc_data_source_config = inc_data_source_config
        # 索引类型
        self.index_type = index_type
        # 回流触发模式
        self.trigger_mode = trigger_mode
        # Topic过期时间
        self.ttl = ttl

    def validate(self):
        if self.field_map:
            self.field_map.validate()
        if self.full_data_source_config:
            self.full_data_source_config.validate()
        if self.inc_data_source_config:
            self.inc_data_source_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.field_map is not None:
            result['fieldMap'] = self.field_map.to_map()
        if self.full_data_source_config is not None:
            result['fullDataSourceConfig'] = self.full_data_source_config.to_map()
        if self.inc_data_source_config is not None:
            result['incDataSourceConfig'] = self.inc_data_source_config.to_map()
        if self.index_type is not None:
            result['indexType'] = self.index_type
        if self.trigger_mode is not None:
            result['triggerMode'] = self.trigger_mode
        if self.ttl is not None:
            result['ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('fieldMap') is not None:
            temp_model = UpdateInstanceTableRequestFieldMap()
            self.field_map = temp_model.from_map(m['fieldMap'])
        if m.get('fullDataSourceConfig') is not None:
            temp_model = UpdateInstanceTableRequestFullDataSourceConfig()
            self.full_data_source_config = temp_model.from_map(m['fullDataSourceConfig'])
        if m.get('incDataSourceConfig') is not None:
            temp_model = UpdateInstanceTableRequestIncDataSourceConfig()
            self.inc_data_source_config = temp_model.from_map(m['incDataSourceConfig'])
        if m.get('indexType') is not None:
            self.index_type = m.get('indexType')
        if m.get('triggerMode') is not None:
            self.trigger_mode = m.get('triggerMode')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        return self


class UpdateInstanceTableResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        # code
        self.code = code
        # message
        self.message = message
        # Id of the request
        self.request_id = request_id
        # result
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UpdateInstanceTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateInstanceTableResponseBody = None,
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
            temp_model = UpdateInstanceTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


