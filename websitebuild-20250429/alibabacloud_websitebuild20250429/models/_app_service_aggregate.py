# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class AppServiceAggregate(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        deleted: int = None,
        end_time: str = None,
        esp_biz_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        group: main_models.AppServiceGroup = None,
        instance_biz_id: str = None,
        name: str = None,
        node_list: List[main_models.TreeNode] = None,
        operation_address: main_models.AppOperationAddress = None,
        profile: main_models.AppServiceProfile = None,
        service_type: str = None,
        service_type_text: str = None,
        slug: str = None,
        start_time: str = None,
        status: str = None,
        user_id: str = None,
    ):
        self.biz_id = biz_id
        self.deleted = deleted
        self.end_time = end_time
        self.esp_biz_id = esp_biz_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.group = group
        self.instance_biz_id = instance_biz_id
        self.name = name
        self.node_list = node_list
        self.operation_address = operation_address
        self.profile = profile
        self.service_type = service_type
        self.service_type_text = service_type_text
        self.slug = slug
        self.start_time = start_time
        self.status = status
        self.user_id = user_id

    def validate(self):
        if self.group:
            self.group.validate()
        if self.node_list:
            for v1 in self.node_list:
                 if v1:
                    v1.validate()
        if self.operation_address:
            self.operation_address.validate()
        if self.profile:
            self.profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.esp_biz_id is not None:
            result['EspBizId'] = self.esp_biz_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.group is not None:
            result['Group'] = self.group.to_map()

        if self.instance_biz_id is not None:
            result['InstanceBizId'] = self.instance_biz_id

        if self.name is not None:
            result['Name'] = self.name

        result['NodeList'] = []
        if self.node_list is not None:
            for k1 in self.node_list:
                result['NodeList'].append(k1.to_map() if k1 else None)

        if self.operation_address is not None:
            result['OperationAddress'] = self.operation_address.to_map()

        if self.profile is not None:
            result['Profile'] = self.profile.to_map()

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.service_type_text is not None:
            result['ServiceTypeText'] = self.service_type_text

        if self.slug is not None:
            result['Slug'] = self.slug

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EspBizId') is not None:
            self.esp_biz_id = m.get('EspBizId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Group') is not None:
            temp_model = main_models.AppServiceGroup()
            self.group = temp_model.from_map(m.get('Group'))

        if m.get('InstanceBizId') is not None:
            self.instance_biz_id = m.get('InstanceBizId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.node_list = []
        if m.get('NodeList') is not None:
            for k1 in m.get('NodeList'):
                temp_model = main_models.TreeNode()
                self.node_list.append(temp_model.from_map(k1))

        if m.get('OperationAddress') is not None:
            temp_model = main_models.AppOperationAddress()
            self.operation_address = temp_model.from_map(m.get('OperationAddress'))

        if m.get('Profile') is not None:
            temp_model = main_models.AppServiceProfile()
            self.profile = temp_model.from_map(m.get('Profile'))

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('ServiceTypeText') is not None:
            self.service_type_text = m.get('ServiceTypeText')

        if m.get('Slug') is not None:
            self.slug = m.get('Slug')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

