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
        # The category ID. You can obtain the category ID by using one of the following methods:
        # - Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Configuration Management** > **Media Asset Configuration** > **Category Management** to view the category ID.
        # - Call the [Create a category](https://help.aliyun.com/document_detail/56401.html) operation to create a category. The category ID is the value of the CateId response parameter.
        # - Call the [Get categories and subcategories](https://help.aliyun.com/document_detail/56406.html) operation to query categories. The category ID is the value of the CateId response parameter.
        self.cate_id = cate_id
        # The end time of the creation time, which must be later than the start time. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time must be in UTC.
        self.end_time = end_time
        # The current page number. Default value: **1**.
        self.page_no = page_no
        # The number of entries per page. Default value: **10**. Maximum value: **100**.
        self.page_size = page_size
        # The list of custom IDs. You can specify one or more custom IDs separated by commas (,). You can specify up to 20 custom IDs.
        self.reference_ids = reference_ids
        # The sorting method of the query results. Valid values:
        # 
        # - **CreationTime:Desc** (default): Sort by creation time in descending order.
        # - **CreationTime:Asc**: Sort by creation time in ascending order.
        self.sort_by = sort_by
        # The start time of the creation time. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time must be in UTC.
        self.start_time = start_time
        # The video status. You can specify multiple statuses separated by commas (,). Valid values:
        # 
        # - **Uploading**: The video is being uploaded.
        # - **UploadFail**: The video failed to be uploaded.
        # - **UploadSucc**: The video is uploaded.
        # - **Transcoding**: The video is being transcoded.
        # - **TranscodeFail**: The video failed to be transcoded.
        # - **Checking**: The video is being reviewed.
        # - **Blocked**: The video is blocked.
        # - **Normal**: The video is normal.
        # - **ProduceFail**: The video failed to be produced.
        # 
        # For more information about the definitions and limits of video statuses, refer to [Status: video status](~~52839#section-p7c-jgy-070~~).
        self.status = status
        # The storage address of the audio or video file.
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

