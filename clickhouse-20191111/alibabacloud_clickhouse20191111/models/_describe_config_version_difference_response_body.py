# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeConfigVersionDifferenceResponseBody(DaraModel):
    def __init__(
        self,
        new_config_xml: str = None,
        old_config_xml: str = None,
        request_id: str = None,
    ):
        # The values of the configuration parameters after the values of the configuration parameters are changed.
        self.new_config_xml = new_config_xml
        # The values of the configuration parameters before the values of the configuration parameters are changed.
        self.old_config_xml = old_config_xml
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_config_xml is not None:
            result['NewConfigXML'] = self.new_config_xml

        if self.old_config_xml is not None:
            result['OldConfigXML'] = self.old_config_xml

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewConfigXML') is not None:
            self.new_config_xml = m.get('NewConfigXML')

        if m.get('OldConfigXML') is not None:
            self.old_config_xml = m.get('OldConfigXML')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

