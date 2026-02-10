# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHoneypotProbeUuidRequest(DaraModel):
    def __init__(
        self,
        control_node_id: str = None,
        lang: str = None,
        probe_type: str = None,
    ):
        # The ID of the management node.
        # 
        # >  You can call the [ListHoneypotNode](~~ListHoneypotNode~~) operation to obtain the ID.
        self.control_node_id = control_node_id
        # The language of the content within the request and the response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The type of the probe. Valid values:
        # 
        # *   **host_probe**: host probe
        # *   **vpc_black_hole_probe**: virtual private cloud (VPC) probe
        self.probe_type = probe_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_node_id is not None:
            result['ControlNodeId'] = self.control_node_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.probe_type is not None:
            result['ProbeType'] = self.probe_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlNodeId') is not None:
            self.control_node_id = m.get('ControlNodeId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProbeType') is not None:
            self.probe_type = m.get('ProbeType')

        return self

