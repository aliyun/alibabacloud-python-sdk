# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribePortAutoCcStatusResponseBody(DaraModel):
    def __init__(
        self,
        port_auto_cc_status: List[main_models.DescribePortAutoCcStatusResponseBodyPortAutoCcStatus] = None,
        request_id: str = None,
    ):
        # An array that consists of the configurations of the Intelligent Protection policy.
        self.port_auto_cc_status = port_auto_cc_status
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.port_auto_cc_status:
            for v1 in self.port_auto_cc_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PortAutoCcStatus'] = []
        if self.port_auto_cc_status is not None:
            for k1 in self.port_auto_cc_status:
                result['PortAutoCcStatus'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.port_auto_cc_status = []
        if m.get('PortAutoCcStatus') is not None:
            for k1 in m.get('PortAutoCcStatus'):
                temp_model = main_models.DescribePortAutoCcStatusResponseBodyPortAutoCcStatus()
                self.port_auto_cc_status.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePortAutoCcStatusResponseBodyPortAutoCcStatus(DaraModel):
    def __init__(
        self,
        mode: str = None,
        switch: str = None,
        web_mode: str = None,
        web_switch: str = None,
    ):
        # The mode of the Intelligent Protection policy. Valid values:
        # 
        # *   **normal**
        # *   **loose**
        # *   **strict**
        self.mode = mode
        # The status of the Intelligent Protection policy. Valid values:
        # 
        # *   **on**: enabled
        # *   **off**: disabled
        self.switch = switch
        # The protection mode for ports 80 and 443. Valid values:
        # 
        # *   **normal**
        # *   **loose**
        # *   **strict**
        self.web_mode = web_mode
        # The status of the Intelligent Protection policy for ports 80 and 443. Valid values:
        # 
        # *   **on**: enabled
        # *   **off**: disabled
        self.web_switch = web_switch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['Mode'] = self.mode

        if self.switch is not None:
            result['Switch'] = self.switch

        if self.web_mode is not None:
            result['WebMode'] = self.web_mode

        if self.web_switch is not None:
            result['WebSwitch'] = self.web_switch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Switch') is not None:
            self.switch = m.get('Switch')

        if m.get('WebMode') is not None:
            self.web_mode = m.get('WebMode')

        if m.get('WebSwitch') is not None:
            self.web_switch = m.get('WebSwitch')

        return self

