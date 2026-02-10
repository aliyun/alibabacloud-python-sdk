# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class StartHoneypotResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.StartHoneypotResponseBodyData = None,
        request_id: str = None,
    ):
        # The information about the honeypot.
        self.data = data
        # The request ID.
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
            temp_model = main_models.StartHoneypotResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class StartHoneypotResponseBodyData(DaraModel):
    def __init__(
        self,
        control_node_name: str = None,
        honeypot_id: str = None,
        honeypot_image_display_name: str = None,
        honeypot_image_name: str = None,
        honeypot_name: str = None,
        node_id: str = None,
        preset_id: str = None,
        state: List[str] = None,
    ):
        # The name of the management node to which the honeypot belongs.
        self.control_node_name = control_node_name
        # The ID of the honeypot.
        self.honeypot_id = honeypot_id
        # The display name of the image.
        self.honeypot_image_display_name = honeypot_image_display_name
        # The name of the image that is used for the honeypot.
        self.honeypot_image_name = honeypot_image_name
        # The custom name of the honeypot.
        self.honeypot_name = honeypot_name
        # The ID of the management node.
        self.node_id = node_id
        # The ID of the custom configuration for the honeypot.
        self.preset_id = preset_id
        # The statuses of the honeypots.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_node_name is not None:
            result['ControlNodeName'] = self.control_node_name

        if self.honeypot_id is not None:
            result['HoneypotId'] = self.honeypot_id

        if self.honeypot_image_display_name is not None:
            result['HoneypotImageDisplayName'] = self.honeypot_image_display_name

        if self.honeypot_image_name is not None:
            result['HoneypotImageName'] = self.honeypot_image_name

        if self.honeypot_name is not None:
            result['HoneypotName'] = self.honeypot_name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.preset_id is not None:
            result['PresetId'] = self.preset_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlNodeName') is not None:
            self.control_node_name = m.get('ControlNodeName')

        if m.get('HoneypotId') is not None:
            self.honeypot_id = m.get('HoneypotId')

        if m.get('HoneypotImageDisplayName') is not None:
            self.honeypot_image_display_name = m.get('HoneypotImageDisplayName')

        if m.get('HoneypotImageName') is not None:
            self.honeypot_image_name = m.get('HoneypotImageName')

        if m.get('HoneypotName') is not None:
            self.honeypot_name = m.get('HoneypotName')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PresetId') is not None:
            self.preset_id = m.get('PresetId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

