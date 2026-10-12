# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListImagesRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        image_uri: str = None,
        labels: str = None,
        name: str = None,
        options: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        query: str = None,
        sort_by: str = None,
        verbose: bool = None,
        workspace_id: str = None,
    ):
        # The visibility of the image. Currently only takes effect for custom images.
        # 
        # - PUBLIC: Public.
        # - PRIVATE: Private.
        self.accessibility = accessibility
        # The image URI.
        self.image_uri = image_uri
        # The label filter conditions. Separate multiple conditions with commas (,).
        # The format of a single filter condition is `Key=Value`.
        # Valid values of Key:
        # 
        # - system.chipType
        # - system.dsw.cudaVersion
        # - system.dsw.fromImageId
        # - system.dsw.fromInstanceId
        # - system.dsw.id
        # - system.dsw.os
        # - system.dsw.osVersion
        # - system.dsw.resourceType
        # - system.dsw.rootImageId
        # - system.dsw.stage
        # - system.dsw.tag
        # - system.dsw.type
        # - system.framework
        # - system.origin
        # - system.pythonVersion
        # - system.source
        # - system.supported.dlc
        # - system.supported.dsw
        self.labels = labels
        # The image name. Fuzzy match is supported.
        self.name = name
        # The options. Currently supports ExactMatchName for exact match search on Name.
        self.options = options
        # The sort order for the specified sort field in a paged query. Used together with SortBy. Default value: ASC.
        # - ASC: Ascending order.
        # - DESC: Descending order.
        self.order = order
        # The page number of the image list. Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page for a paged query. Default value: 20.
        self.page_size = page_size
        # Fuzzy searches by image name and description.
        self.query = query
        # The sort field for a paged query. Currently, the GmtCreateTime field is used for sorting.
        self.sort_by = sort_by
        # Specifies whether to display non-essential information. Non-essential information currently includes Labels. Valid values:
        # 
        # - true: Includes non-essential information.
        # - false: Does not include non-essential information.
        self.verbose = verbose
        # The workspace ID. For information about how to obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
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

        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.name is not None:
            result['Name'] = self.name

        if self.options is not None:
            result['Options'] = self.options

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query is not None:
            result['Query'] = self.query

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.verbose is not None:
            result['Verbose'] = self.verbose

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

