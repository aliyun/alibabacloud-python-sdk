# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyvmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class ListServiceInstanceForPageResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        message: str = None,
        model: main_models.ListServiceInstanceForPageResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        # 状态码，OK表示响应成功
        self.code = code
        # 响应消息
        self.message = message
        self.model = model
        # 请求唯一id
        self.request_id = request_id
        # 是否成功
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            temp_model = main_models.ListServiceInstanceForPageResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListServiceInstanceForPageResponseBodyModel(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        records: List[main_models.ListServiceInstanceForPageResponseBodyModelRecords] = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # 当前页码
        self.page_no = page_no
        # 每页数量
        self.page_size = page_size
        self.records = records
        # 总数
        self.total_count = total_count
        # 总页数
        self.total_page = total_page

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.ListServiceInstanceForPageResponseBodyModelRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListServiceInstanceForPageResponseBodyModelRecords(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        code: str = None,
        gmt_create: str = None,
        instance_status: str = None,
        name: str = None,
        relation_available_count: int = None,
        relation_total_count: int = None,
        scene_id: int = None,
        scene_name: str = None,
        status: str = None,
        usage_id: int = None,
        usage_name: str = None,
    ):
        # aliUid
        self.ali_uid = ali_uid
        # 服务实例号
        self.code = code
        # 创建时间（时间戳）
        self.gmt_create = gmt_create
        # 实例状态（init：初始化；usable：可用；unusable：不可用；destory：注销）
        self.instance_status = instance_status
        # 服务实例名称
        self.name = name
        # 关联可用数量
        self.relation_available_count = relation_available_count
        # 关联总数量
        self.relation_total_count = relation_total_count
        # 场景ID
        self.scene_id = scene_id
        # 场景名称
        self.scene_name = scene_name
        # 绑定状态：绑定；未绑定
        self.status = status
        # 用途ID
        self.usage_id = usage_id
        # 用途名称
        self.usage_name = usage_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.code is not None:
            result['Code'] = self.code

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.name is not None:
            result['Name'] = self.name

        if self.relation_available_count is not None:
            result['RelationAvailableCount'] = self.relation_available_count

        if self.relation_total_count is not None:
            result['RelationTotalCount'] = self.relation_total_count

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        if self.status is not None:
            result['Status'] = self.status

        if self.usage_id is not None:
            result['UsageId'] = self.usage_id

        if self.usage_name is not None:
            result['UsageName'] = self.usage_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RelationAvailableCount') is not None:
            self.relation_available_count = m.get('RelationAvailableCount')

        if m.get('RelationTotalCount') is not None:
            self.relation_total_count = m.get('RelationTotalCount')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UsageId') is not None:
            self.usage_id = m.get('UsageId')

        if m.get('UsageName') is not None:
            self.usage_name = m.get('UsageName')

        return self

