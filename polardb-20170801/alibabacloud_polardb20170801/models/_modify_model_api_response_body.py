# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyModelApiResponseBody(DaraModel):
    def __init__(
        self,
        category: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        model_api_id: str = None,
        model_mappings: str = None,
        model_routing: str = None,
        name: str = None,
        path_prefix: str = None,
        protocol: str = None,
        request_id: str = None,
        route_rules: str = None,
        status: str = None,
    ):
        # The category of the model.
        self.category = category
        # The time when the model API was created.
        self.gmt_created = gmt_created
        # The time when the model API was last updated.
        self.gmt_modified = gmt_modified
        # The ID of the model API.
        self.model_api_id = model_api_id
        # The current model name mappings, returned as a JSON array string. This parameter is empty if no mappings are configured.
        self.model_mappings = model_mappings
        # The current intelligent routing candidate list, returned as a JSON object string.
        self.model_routing = model_routing
        # The updated name of the model API.
        self.name = name
        # The API path prefix.
        self.path_prefix = path_prefix
        # The access protocol.
        self.protocol = protocol
        # The request ID.
        self.request_id = request_id
        # The current routing rules, returned as a JSON string. A byte-for-byte exact match of the input is not guaranteed.
        self.route_rules = route_rules
        # The status of the model API.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.model_api_id is not None:
            result['ModelApiId'] = self.model_api_id

        if self.model_mappings is not None:
            result['ModelMappings'] = self.model_mappings

        if self.model_routing is not None:
            result['ModelRouting'] = self.model_routing

        if self.name is not None:
            result['Name'] = self.name

        if self.path_prefix is not None:
            result['PathPrefix'] = self.path_prefix

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.route_rules is not None:
            result['RouteRules'] = self.route_rules

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ModelApiId') is not None:
            self.model_api_id = m.get('ModelApiId')

        if m.get('ModelMappings') is not None:
            self.model_mappings = m.get('ModelMappings')

        if m.get('ModelRouting') is not None:
            self.model_routing = m.get('ModelRouting')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PathPrefix') is not None:
            self.path_prefix = m.get('PathPrefix')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RouteRules') is not None:
            self.route_rules = m.get('RouteRules')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

