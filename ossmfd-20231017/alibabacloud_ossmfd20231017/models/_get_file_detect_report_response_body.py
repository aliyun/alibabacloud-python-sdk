# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ossmfd20231017 import models as main_models
from darabonba.model import DaraModel

class GetFileDetectReportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetFileDetectReportResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = main_models.GetFileDetectReportResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetFileDetectReportResponseBodyData(DaraModel):
    def __init__(
        self,
        basic: str = None,
        file_hash: str = None,
        filename: str = None,
        has_data: bool = None,
        intelligences: str = None,
        sandbox: str = None,
        show_tab: bool = None,
        threat_level: int = None,
        threat_types: str = None,
    ):
        self.basic = basic
        self.file_hash = file_hash
        self.filename = filename
        self.has_data = has_data
        self.intelligences = intelligences
        self.sandbox = sandbox
        self.show_tab = show_tab
        self.threat_level = threat_level
        self.threat_types = threat_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic is not None:
            result['Basic'] = self.basic

        if self.file_hash is not None:
            result['FileHash'] = self.file_hash

        if self.filename is not None:
            result['Filename'] = self.filename

        if self.has_data is not None:
            result['HasData'] = self.has_data

        if self.intelligences is not None:
            result['Intelligences'] = self.intelligences

        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox

        if self.show_tab is not None:
            result['ShowTab'] = self.show_tab

        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level

        if self.threat_types is not None:
            result['ThreatTypes'] = self.threat_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Basic') is not None:
            self.basic = m.get('Basic')

        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')

        if m.get('Filename') is not None:
            self.filename = m.get('Filename')

        if m.get('HasData') is not None:
            self.has_data = m.get('HasData')

        if m.get('Intelligences') is not None:
            self.intelligences = m.get('Intelligences')

        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')

        if m.get('ShowTab') is not None:
            self.show_tab = m.get('ShowTab')

        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')

        if m.get('ThreatTypes') is not None:
            self.threat_types = m.get('ThreatTypes')

        return self

