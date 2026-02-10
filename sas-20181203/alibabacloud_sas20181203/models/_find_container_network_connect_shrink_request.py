# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FindContainerNetworkConnectShrinkRequest(DaraModel):
    def __init__(
        self,
        criteria_type: str = None,
        current_page: int = None,
        dst_node_shrink: str = None,
        end_time: int = None,
        page_size: int = None,
        src_node_shrink: str = None,
        start_time: int = None,
    ):
        # The type of the information that you want to query. Valid values:
        # 
        # *   **EDGE**: connection information
        self.criteria_type = criteria_type
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The information about the destination node.
        self.dst_node_shrink = dst_node_shrink
        # The end time of the network connection.
        self.end_time = end_time
        # The number of entries to return on each page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The information about the source node.
        self.src_node_shrink = src_node_shrink
        # The start time of the network connection.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.criteria_type is not None:
            result['CriteriaType'] = self.criteria_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dst_node_shrink is not None:
            result['DstNode'] = self.dst_node_shrink

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.src_node_shrink is not None:
            result['SrcNode'] = self.src_node_shrink

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CriteriaType') is not None:
            self.criteria_type = m.get('CriteriaType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DstNode') is not None:
            self.dst_node_shrink = m.get('DstNode')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SrcNode') is not None:
            self.src_node_shrink = m.get('SrcNode')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

