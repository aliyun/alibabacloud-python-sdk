# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetRetcodeLogstoreResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetRetcodeLogstoreResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned struct.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetRetcodeLogstoreResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetRetcodeLogstoreResponseBodyData(DaraModel):
    def __init__(
        self,
        message: str = None,
        retcode_slsconfig: main_models.GetRetcodeLogstoreResponseBodyDataRetcodeSLSConfig = None,
        status: str = None,
    ):
        # The content of the log.
        self.message = message
        # The information about Log Service.
        self.retcode_slsconfig = retcode_slsconfig
        # The status of the request.
        self.status = status

    def validate(self):
        if self.retcode_slsconfig:
            self.retcode_slsconfig.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.retcode_slsconfig is not None:
            result['RetcodeSLSConfig'] = self.retcode_slsconfig.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RetcodeSLSConfig') is not None:
            temp_model = main_models.GetRetcodeLogstoreResponseBodyDataRetcodeSLSConfig()
            self.retcode_slsconfig = temp_model.from_map(m.get('RetcodeSLSConfig'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetRetcodeLogstoreResponseBodyDataRetcodeSLSConfig(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
        region_id: str = None,
    ):
        # The Log Service Logstore.
        self.logstore = logstore
        # The Log Service project.
        self.project = project
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logstore is not None:
            result['Logstore'] = self.logstore

        if self.project is not None:
            result['Project'] = self.project

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

