# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class DeleteTraceAppRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        delete_reason: main_models.DeleteTraceAppRequestDeleteReason = None,
        pid: str = None,
        region_id: str = None,
        type: str = None,
    ):
        # The ID of the application that you want to delete. You can call the SearchTraceAppByName operation to query the application ID. For more information, see [SearchTraceAppByName](https://help.aliyun.com/document_detail/130676.html).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The reason(s) to delete application.
        self.delete_reason = delete_reason
        # The PID of the application. For more information about how to query the PID, see [QueryMetricByPage](https://www.alibabacloud.com/help/zh/doc-detail/186100.htm?spm=a2cdw.13409063.0.0.7a72281f0bkTfx#title-imy-7gj-qhr).
        # 
        # This parameter is required.
        self.pid = pid
        # The ID of the region in which the application is located.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The type of the application that you want to delete. You can call the SearchTraceAppByName operation to query the application type. For more information, see [SearchTraceAppByName](https://help.aliyun.com/document_detail/130676.html). Valid values:
        # 
        # *   `TRACE`: Application Monitoring
        # *   `RETCODE`: frontend monitoring
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.delete_reason:
            self.delete_reason.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.delete_reason is not None:
            result['DeleteReason'] = self.delete_reason.to_map()

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DeleteReason') is not None:
            temp_model = main_models.DeleteTraceAppRequestDeleteReason()
            self.delete_reason = temp_model.from_map(m.get('DeleteReason'))

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DeleteTraceAppRequestDeleteReason(DaraModel):
    def __init__(
        self,
        reason_ids: List[main_models.DeleteTraceAppRequestDeleteReasonReasonIds] = None,
        remark: str = None,
    ):
        # Reasons Ids.
        self.reason_ids = reason_ids
        # Additional remarks when none of the reasons for removal provided are met.
        self.remark = remark

    def validate(self):
        if self.reason_ids:
            for v1 in self.reason_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ReasonIds'] = []
        if self.reason_ids is not None:
            for k1 in self.reason_ids:
                result['ReasonIds'].append(k1.to_map() if k1 else None)

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.reason_ids = []
        if m.get('ReasonIds') is not None:
            for k1 in m.get('ReasonIds'):
                temp_model = main_models.DeleteTraceAppRequestDeleteReasonReasonIds()
                self.reason_ids.append(temp_model.from_map(k1))

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

class DeleteTraceAppRequestDeleteReasonReasonIds(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The ID of the reason for deletion.
        self.id = id
        # A description of the reason for removal.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

