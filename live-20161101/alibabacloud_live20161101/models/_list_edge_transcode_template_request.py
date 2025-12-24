# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEdgeTranscodeTemplateRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        keyword: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        region_id: str = None,
        sort_by: str = None,
        type: str = None,
        video_codec: str = None,
    ):
        # The ID of the data center.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The keyword of the query.
        # 
        # *   You can specify a template ID for an exact match.
        # *   You can also specify a template name for a fuzzy match.
        self.keyword = keyword
        self.owner_id = owner_id
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        self.region_id = region_id
        # The sorting order of the templates by creation time. Default value: desc. Valid values:
        # 
        # *   desc: descending order.
        # *   asc: ascending order.
        self.sort_by = sort_by
        # The type of edge transcoding. Valid values:
        # 
        # *   **common**: standard transcoding and Narrowband HD™ 1.0 transcoding.
        # *   **nbhd-2**: Narrowband HD™ 2.0 transcoding.
        # *   **ultra-hd**: ultra-high definition transcoding.
        # 
        # >  If you do not specify this parameter, the query result is filtered based on the type of edge transcoding on which you are granted permissions.
        self.type = type
        # The video encoding format. Valid values:
        # 
        # *   H.264
        # *   H.265
        # 
        # >  If you do not specify this parameter, the query result is filtered based on the video encoding format on which you are granted permissions.
        self.video_codec = video_codec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.type is not None:
            result['Type'] = self.type

        if self.video_codec is not None:
            result['VideoCodec'] = self.video_codec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VideoCodec') is not None:
            self.video_codec = m.get('VideoCodec')

        return self

