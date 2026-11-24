# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateModelApiResponseBody(DaraModel):
    def __init__(
        self,
        category: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        invoke_endpoint: str = None,
        model_api_id: str = None,
        model_mappings: str = None,
        name: str = None,
        path_prefix: str = None,
        protocol: str = None,
        request_id: str = None,
        route_rules: str = None,
        status: str = None,
    ):
        # The model category.
        self.category = category
        # The creation time.
        self.gmt_created = gmt_created
        # The modification time.
        self.gmt_modified = gmt_modified
        # The invocation endpoint.
        self.invoke_endpoint = invoke_endpoint
        # The model API ID.
        self.model_api_id = model_api_id
        # The saved model name mappings, returned as a JSON array string. This parameter is empty if no mappings are configured.
        self.model_mappings = model_mappings
        # The name of the model API.
        self.name = name
        # The invocation path prefix.
        self.path_prefix = path_prefix
        # The access protocol.
        self.protocol = protocol
        # The request ID.
        self.request_id = request_id
        # The saved routing rules, returned as a JSON string. A byte-by-byte exact echo is not guaranteed.
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

        if self.invoke_endpoint is not None:
            result['InvokeEndpoint'] = self.invoke_endpoint

        if self.model_api_id is not None:
            result['ModelApiId'] = self.model_api_id

        if self.model_mappings is not None:
            result['ModelMappings'] = self.model_mappings

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

        if m.get('InvokeEndpoint') is not None:
            self.invoke_endpoint = m.get('InvokeEndpoint')

        if m.get('ModelApiId') is not None:
            self.model_api_id = m.get('ModelApiId')

        if m.get('ModelMappings') is not None:
            self.model_mappings = m.get('ModelMappings')

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

