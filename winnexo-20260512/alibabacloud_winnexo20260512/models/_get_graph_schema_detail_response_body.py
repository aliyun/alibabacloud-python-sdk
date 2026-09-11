# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetGraphSchemaDetailResponseBody(DaraModel):
    def __init__(
        self,
        business_profile: str = None,
        code: str = None,
        content_hash: str = None,
        created_by: str = None,
        display_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        graph_name: str = None,
        graph_status: str = None,
        has_draft: bool = None,
        message: str = None,
        request_id: str = None,
        schema_version: str = None,
        yaml_edit: str = None,
    ):
        # The business description of the graph. An empty string is returned if this parameter is not configured.
        self.business_profile = business_profile
        # The status code.
        self.code = code
        # The hash fingerprint of the schema content.
        self.content_hash = content_hash
        # The creator.
        self.created_by = created_by
        # The display name.
        self.display_name = display_name
        # The creation time.
        self.gmt_create = gmt_create
        # The last update time.
        self.gmt_modified = gmt_modified
        # The name of the graph.
        self.graph_name = graph_name
        # The status of the semantic graph.
        self.graph_status = graph_status
        # Indicates whether the graph contains a draft.
        self.has_draft = has_draft
        # The prompt message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The version.
        self.schema_version = schema_version
        # The original YAML text of the graph schema trimmed by READ permission. The $ref references within the authorized subgraph are retained.
        self.yaml_edit = yaml_edit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_profile is not None:
            result['businessProfile'] = self.business_profile

        if self.code is not None:
            result['code'] = self.code

        if self.content_hash is not None:
            result['contentHash'] = self.content_hash

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.graph_name is not None:
            result['graphName'] = self.graph_name

        if self.graph_status is not None:
            result['graphStatus'] = self.graph_status

        if self.has_draft is not None:
            result['hasDraft'] = self.has_draft

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.schema_version is not None:
            result['schemaVersion'] = self.schema_version

        if self.yaml_edit is not None:
            result['yamlEdit'] = self.yaml_edit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessProfile') is not None:
            self.business_profile = m.get('businessProfile')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('contentHash') is not None:
            self.content_hash = m.get('contentHash')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('graphName') is not None:
            self.graph_name = m.get('graphName')

        if m.get('graphStatus') is not None:
            self.graph_status = m.get('graphStatus')

        if m.get('hasDraft') is not None:
            self.has_draft = m.get('hasDraft')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('schemaVersion') is not None:
            self.schema_version = m.get('schemaVersion')

        if m.get('yamlEdit') is not None:
            self.yaml_edit = m.get('yamlEdit')

        return self

