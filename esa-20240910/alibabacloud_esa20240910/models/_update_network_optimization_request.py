# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNetworkOptimizationRequest(DaraModel):
    def __init__(
        self,
        config_id: int = None,
        grpc: str = None,
        http_2origin: str = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        site_id: int = None,
        smart_routing: str = None,
        upload_max_filesize: str = None,
        websocket: str = None,
    ):
        # Configuration ID.
        # 
        # This parameter is required.
        self.config_id = config_id
        # Whether to enable GRPC, default is disabled. Possible values:
        # - on: Enable
        # - off: Disable
        self.grpc = grpc
        # Whether to enable HTTP2 origin, default is disabled. Possible values:
        # - on: Enable
        # - off: Disable
        self.http_2origin = http_2origin
        # Rule content, using conditional expressions to match user requests. This parameter is not required when adding a global configuration. There are two usage scenarios:
        # - Match all incoming requests: Set the value to true
        # - Match specific requests: Set the value to a custom expression, for example: (http.host eq \\"video.example.com\\")
        self.rule = rule
        # Rule switch. This parameter is not required when adding a global configuration. Possible values:
        # - on: Enable.
        # - off: Disable.
        self.rule_enable = rule_enable
        # Rule name. This parameter is not required when adding a global configuration.
        self.rule_name = rule_name
        self.sequence = sequence
        # Site ID, which can be obtained by calling the [ListSites](~~ListSites~~) API.
        # 
        # This parameter is required.
        self.site_id = site_id
        # Whether to enable the smart routing service, default is disabled. Possible values:
        # - on: Enable
        # - off: Disable
        self.smart_routing = smart_routing
        # Maximum upload file size, in MB, with a range of 100 to 500.
        self.upload_max_filesize = upload_max_filesize
        # Whether to enable Websocket, default is enabled. Possible values:
        # - on: Enable
        # - off: Disable
        self.websocket = websocket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.grpc is not None:
            result['Grpc'] = self.grpc

        if self.http_2origin is not None:
            result['Http2Origin'] = self.http_2origin

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.smart_routing is not None:
            result['SmartRouting'] = self.smart_routing

        if self.upload_max_filesize is not None:
            result['UploadMaxFilesize'] = self.upload_max_filesize

        if self.websocket is not None:
            result['Websocket'] = self.websocket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('Grpc') is not None:
            self.grpc = m.get('Grpc')

        if m.get('Http2Origin') is not None:
            self.http_2origin = m.get('Http2Origin')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SmartRouting') is not None:
            self.smart_routing = m.get('SmartRouting')

        if m.get('UploadMaxFilesize') is not None:
            self.upload_max_filesize = m.get('UploadMaxFilesize')

        if m.get('Websocket') is not None:
            self.websocket = m.get('Websocket')

        return self

