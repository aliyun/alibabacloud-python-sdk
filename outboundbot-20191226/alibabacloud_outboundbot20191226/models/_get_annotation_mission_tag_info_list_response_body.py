# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class GetAnnotationMissionTagInfoListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAnnotationMissionTagInfoListResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetAnnotationMissionTagInfoListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAnnotationMissionTagInfoListResponseBodyData(DaraModel):
    def __init__(
        self,
        annotation_mission_tag_info_list: List[main_models.GetAnnotationMissionTagInfoListResponseBodyDataAnnotationMissionTagInfoList] = None,
        message: str = None,
        success: bool = None,
    ):
        self.annotation_mission_tag_info_list = annotation_mission_tag_info_list
        self.message = message
        self.success = success

    def validate(self):
        if self.annotation_mission_tag_info_list:
            for v1 in self.annotation_mission_tag_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AnnotationMissionTagInfoList'] = []
        if self.annotation_mission_tag_info_list is not None:
            for k1 in self.annotation_mission_tag_info_list:
                result['AnnotationMissionTagInfoList'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.annotation_mission_tag_info_list = []
        if m.get('AnnotationMissionTagInfoList') is not None:
            for k1 in m.get('AnnotationMissionTagInfoList'):
                temp_model = main_models.GetAnnotationMissionTagInfoListResponseBodyDataAnnotationMissionTagInfoList()
                self.annotation_mission_tag_info_list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAnnotationMissionTagInfoListResponseBodyDataAnnotationMissionTagInfoList(DaraModel):
    def __init__(
        self,
        annotation_mission_tag_info_description: str = None,
        annotation_mission_tag_info_id: str = None,
        annotation_mission_tag_info_name: str = None,
        delete: bool = None,
        instance_id: str = None,
        tenant_id: str = None,
    ):
        self.annotation_mission_tag_info_description = annotation_mission_tag_info_description
        self.annotation_mission_tag_info_id = annotation_mission_tag_info_id
        self.annotation_mission_tag_info_name = annotation_mission_tag_info_name
        self.delete = delete
        self.instance_id = instance_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation_mission_tag_info_description is not None:
            result['AnnotationMissionTagInfoDescription'] = self.annotation_mission_tag_info_description

        if self.annotation_mission_tag_info_id is not None:
            result['AnnotationMissionTagInfoId'] = self.annotation_mission_tag_info_id

        if self.annotation_mission_tag_info_name is not None:
            result['AnnotationMissionTagInfoName'] = self.annotation_mission_tag_info_name

        if self.delete is not None:
            result['Delete'] = self.delete

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnotationMissionTagInfoDescription') is not None:
            self.annotation_mission_tag_info_description = m.get('AnnotationMissionTagInfoDescription')

        if m.get('AnnotationMissionTagInfoId') is not None:
            self.annotation_mission_tag_info_id = m.get('AnnotationMissionTagInfoId')

        if m.get('AnnotationMissionTagInfoName') is not None:
            self.annotation_mission_tag_info_name = m.get('AnnotationMissionTagInfoName')

        if m.get('Delete') is not None:
            self.delete = m.get('Delete')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

