# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVideoListRequest(DaraModel):
    def __init__(
        self,
        cate_id: int = None,
        end_time: str = None,
        page_no: int = None,
        page_size: int = None,
        sort_by: str = None,
        start_time: str = None,
        status: str = None,
    ):
        # The ID of the category.
        self.cate_id = cate_id
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The sorting method of the results. Valid values:
        # 
        # *   CreationTime:Desc (default): sorts results in reverse chronological order.
        # *   CreationTime:Asc: sorts results in chronological order.
        self.sort_by = sort_by
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time
        # The status of the video. You can specify multiple video statuses and separate them with commas (,).
        # 
        # Valid values:
        # 
        # *   PrepareFail: The file is abnormal.
        # *   UploadFail: The video failed to be uploaded.
        # *   UploadSucc: The video is uploaded.
        # *   Transcoding: The video is being transcoded.
        # *   TranscodeFail: The video failed to be transcoded.
        # *   ProduceFail: The video failed to be produced.
        # *   Normal: The video is normal.
        # *   Uploading: The video is being uploaded.
        # *   Preparing: The file is being generated.
        # *   Blocked: The video is blocked.
        # *   checking: The video is being reviewed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

