# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class CreateWorkerBootstrapTokenResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateWorkerBootstrapTokenResponseBodyData = None,
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
            temp_model = main_models.CreateWorkerBootstrapTokenResponseBodyData()
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

class CreateWorkerBootstrapTokenResponseBodyData(DaraModel):
    def __init__(
        self,
        bootstrap_token: str = None,
        cms: main_models.CreateWorkerBootstrapTokenResponseBodyDataCms = None,
        instance_id: str = None,
        name: str = None,
        network_type: str = None,
        token_fingerprint: str = None,
    ):
        self.bootstrap_token = bootstrap_token
        self.cms = cms
        self.instance_id = instance_id
        self.name = name
        self.network_type = network_type
        self.token_fingerprint = token_fingerprint

    def validate(self):
        if self.cms:
            self.cms.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bootstrap_token is not None:
            result['BootstrapToken'] = self.bootstrap_token

        if self.cms is not None:
            result['Cms'] = self.cms.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.token_fingerprint is not None:
            result['TokenFingerprint'] = self.token_fingerprint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BootstrapToken') is not None:
            self.bootstrap_token = m.get('BootstrapToken')

        if m.get('Cms') is not None:
            temp_model = main_models.CreateWorkerBootstrapTokenResponseBodyDataCms()
            self.cms = temp_model.from_map(m.get('Cms'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('TokenFingerprint') is not None:
            self.token_fingerprint = m.get('TokenFingerprint')

        return self

class CreateWorkerBootstrapTokenResponseBodyDataCms(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        license_key: str = None,
        workspace: str = None,
    ):
        self.endpoint = endpoint
        self.license_key = license_key
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.license_key is not None:
            result['LicenseKey'] = self.license_key

        if self.workspace is not None:
            result['Workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('LicenseKey') is not None:
            self.license_key = m.get('LicenseKey')

        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')

        return self

