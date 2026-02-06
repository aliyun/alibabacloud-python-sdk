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
        reference_ids: str = None,
        sort_by: str = None,
        start_time: str = None,
        status: str = None,
        storage_location: str = None,
    ):
        # The ID of the category. You can use one of the following methods to obtain the category ID:
        # 
        # *   Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Configuration Management** > **Media Management** > **Categories** to view the category ID.
        # *   Obtain the value of CateId from the response to the [AddCategory](https://help.aliyun.com/document_detail/56401.html) operation.
        # *   Obtain the value of CateId from the response to the [GetCategories](https://help.aliyun.com/document_detail/56406.html) operation.
        self.cate_id = cate_id
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.end_time = end_time
        # The number of the page to return. Default value: **1**.
        self.page_no = page_no
        # The number of entries to return on each page. Default value: **10**. Maximum value: **100**.
        self.page_size = page_size
        self.reference_ids = reference_ids
        # The sorting method of the results. Valid values:
        # 
        # *   **CreationTime:Desc** (default): The results are sorted in reverse chronological order based on the creation time.
        # *   **CreationTime:Asc**: The results are sorted in chronological order based on the creation time.
        self.sort_by = sort_by
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.start_time = start_time
        # The status of the video. You can specify multiple video statuses and separate them with commas (,). Valid values:
        # 
        # *   **Uploading**: The video is being uploaded.
        # *   **UploadFail**: The video failed to be uploaded.
        # *   **UploadSucc**: The video has been uploaded.
        # *   **Transcoding**: The video is being transcoded.
        # *   **TranscodeFail**: The video failed to be transcoded.
        # *   **checking**: The video is being reviewed.
        # *   **Blocked**: The video is blocked.
        # *   **Normal**: The video is normal.
        # *   **ProduceFail**: The video failed to be produced.
        # 
        # For more information about each video status, see the "Status: the status of a video" section of the [Basic data types](~~52839#section-p7c-jgy-070~~) topic.
        self.status = status
        # The storage address of the media file.
        self.storage_location = storage_location

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

        if self.reference_ids is not None:
            result['ReferenceIds'] = self.reference_ids

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

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

        if m.get('ReferenceIds') is not None:
            self.reference_ids = m.get('ReferenceIds')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        return self

