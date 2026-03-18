# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class GetNodeGroupFeatureGateResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: main_models.GetNodeGroupFeatureGateResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # AccessDeniedDetail
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Data') is not None:
            temp_model = main_models.GetNodeGroupFeatureGateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetNodeGroupFeatureGateResponseBodyData(DaraModel):
    def __init__(
        self,
        need_restart_after_modify_disk_size: bool = None,
        support_fast_mode_modify_resource: bool = None,
        support_fast_restart: bool = None,
        support_modify_spec_type: bool = None,
    ):
        self.need_restart_after_modify_disk_size = need_restart_after_modify_disk_size
        self.support_fast_mode_modify_resource = support_fast_mode_modify_resource
        self.support_fast_restart = support_fast_restart
        self.support_modify_spec_type = support_modify_spec_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.need_restart_after_modify_disk_size is not None:
            result['NeedRestartAfterModifyDiskSize'] = self.need_restart_after_modify_disk_size

        if self.support_fast_mode_modify_resource is not None:
            result['SupportFastModeModifyResource'] = self.support_fast_mode_modify_resource

        if self.support_fast_restart is not None:
            result['SupportFastRestart'] = self.support_fast_restart

        if self.support_modify_spec_type is not None:
            result['SupportModifySpecType'] = self.support_modify_spec_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NeedRestartAfterModifyDiskSize') is not None:
            self.need_restart_after_modify_disk_size = m.get('NeedRestartAfterModifyDiskSize')

        if m.get('SupportFastModeModifyResource') is not None:
            self.support_fast_mode_modify_resource = m.get('SupportFastModeModifyResource')

        if m.get('SupportFastRestart') is not None:
            self.support_fast_restart = m.get('SupportFastRestart')

        if m.get('SupportModifySpecType') is not None:
            self.support_modify_spec_type = m.get('SupportModifySpecType')

        return self

