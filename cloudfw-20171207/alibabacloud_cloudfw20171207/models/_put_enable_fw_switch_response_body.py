# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class PutEnableFwSwitchResponseBody(DaraModel):
    def __init__(
        self,
        abnormal_resource_status_list: List[main_models.PutEnableFwSwitchResponseBodyAbnormalResourceStatusList] = None,
        dry_run: bool = None,
        request_id: str = None,
    ):
        # The status information list of assets that are not synchronized.
        self.abnormal_resource_status_list = abnormal_resource_status_list
        # Indicates that this is a successful dry run response. A value of true indicates that only the dry run was completed and no real changes were made. This field is not returned or is set to false for real calls.
        self.dry_run = dry_run
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.abnormal_resource_status_list:
            for v1 in self.abnormal_resource_status_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AbnormalResourceStatusList'] = []
        if self.abnormal_resource_status_list is not None:
            for k1 in self.abnormal_resource_status_list:
                result['AbnormalResourceStatusList'].append(k1.to_map() if k1 else None)

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.abnormal_resource_status_list = []
        if m.get('AbnormalResourceStatusList') is not None:
            for k1 in m.get('AbnormalResourceStatusList'):
                temp_model = main_models.PutEnableFwSwitchResponseBodyAbnormalResourceStatusList()
                self.abnormal_resource_status_list.append(temp_model.from_map(k1))

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class PutEnableFwSwitchResponseBodyAbnormalResourceStatusList(DaraModel):
    def __init__(
        self,
        msg: str = None,
        resource: str = None,
        status: str = None,
    ):
        # The message when the asset is not synchronized. Valid values:
        # - cloudfirewall do not sync this ip address: Cloud Firewall has not synchronized this asset IP address.
        self.msg = msg
        # The asset IP address.
        self.resource = resource
        # The status of the asset that is not synchronized. Valid values:
        # - ip_not_sync: The asset is not synchronized.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.msg is not None:
            result['Msg'] = self.msg

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

