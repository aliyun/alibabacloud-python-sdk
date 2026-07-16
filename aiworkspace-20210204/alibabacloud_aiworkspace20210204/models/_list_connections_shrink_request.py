# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListConnectionsShrinkRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        connection_ids_shrink: str = None,
        connection_name: str = None,
        connection_types_shrink: str = None,
        creator: str = None,
        encrypt_option: str = None,
        max_results: int = None,
        model: str = None,
        model_types_shrink: str = None,
        next_token: str = None,
        order: str = None,
        sort_by: str = None,
        tool_call: bool = None,
        workspace_id: str = None,
    ):
        # Visibility of the connection. Valid values:
        # 
        # - PUBLIC: visible to all workspace members.
        # 
        # - PRIVATE: visible only to the creator.
        self.accessibility = accessibility
        # List of connection IDs to filter by.
        self.connection_ids_shrink = connection_ids_shrink
        # Connection name. Supports fuzzy matching.
        self.connection_name = connection_name
        # List of connection types to filter by.
        self.connection_types_shrink = connection_types_shrink
        # Alibaba Cloud account ID of the creator.
        self.creator = creator
        # Encryption option for sensitive fields in the response. Valid values:
        # 
        # - PlainText: returns values in plaintext.
        # 
        # - Secret: returns values in ciphertext.
        self.encrypt_option = encrypt_option
        # Maximum number of entries per page.
        self.max_results = max_results
        # Model identifier. Filters connections associated with this model.
        self.model = model
        # List of model types to filter by.
        self.model_types_shrink = model_types_shrink
        # The token that marks the starting position for the next page of results.
        self.next_token = next_token
        # Sort order. Use with the SortBy parameter. Valid values:
        # 
        # - ASC: ascending order.
        # 
        # - DESC (default): descending order.
        self.order = order
        # Field by which to sort results. Default value: GmtCreateTime. Valid values:
        # 
        # - GmtCreateTime (default): sorts by creation time.
        self.sort_by = sort_by
        # Whether tool calling is supported. Valid values:
        # 
        # - true: supported.
        # 
        # - false: not supported.
        self.tool_call = tool_call
        # Workspace ID. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.connection_ids_shrink is not None:
            result['ConnectionIds'] = self.connection_ids_shrink

        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name

        if self.connection_types_shrink is not None:
            result['ConnectionTypes'] = self.connection_types_shrink

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.encrypt_option is not None:
            result['EncryptOption'] = self.encrypt_option

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.model is not None:
            result['Model'] = self.model

        if self.model_types_shrink is not None:
            result['ModelTypes'] = self.model_types_shrink

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order is not None:
            result['Order'] = self.order

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.tool_call is not None:
            result['ToolCall'] = self.tool_call

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('ConnectionIds') is not None:
            self.connection_ids_shrink = m.get('ConnectionIds')

        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        if m.get('ConnectionTypes') is not None:
            self.connection_types_shrink = m.get('ConnectionTypes')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('EncryptOption') is not None:
            self.encrypt_option = m.get('EncryptOption')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('ModelTypes') is not None:
            self.model_types_shrink = m.get('ModelTypes')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('ToolCall') is not None:
            self.tool_call = m.get('ToolCall')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

