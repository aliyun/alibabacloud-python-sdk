# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDoctorHDFSDirectoriesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        date_time: str = None,
        dir_path: str = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        order_type: str = None,
        region_id: str = None,
    ):
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The date. The value is in the ISO 8601 format. For example, 2023-01-01 represents January 1, 2023.
        # 
        # This parameter is required.
        self.date_time = date_time
        # The path of the directory. The directory depth cannot exceed five levels. If you do not specify this parameter, the analysis results of all directories are returned.
        self.dir_path = dir_path
        # The maximum number of entries to return on each page.
        self.max_results = max_results
        # The token that is used to start the next query.
        self.next_token = next_token
        # The property based on which to sort the query results. Valid values:
        # 
        # - totalFileCount: the total number of files.
        # 
        # - largeFileCount: the number of large files. A large file is 1 GB or larger.
        # 
        # - mediumFileCount: the number of medium-sized files. A medium-sized file is larger than 128 MB and smaller than 1 GB.
        # 
        # - smallFileCount: the number of small files. A small file is larger than 10 MB and less than or equal to 128 MB.
        # 
        # - tinyFileCount: the number of tiny files. A tiny file is larger than 0 MB and less than or equal to 10 MB.
        # 
        # - emptyFileCount: the number of empty files. An empty file is 0 MB in size.
        # 
        # - hotDataSize: the size of hot data. Hot data is data that was accessed in the last 7 days.
        # 
        # - warmDataSize: the size of warm data. Warm data is data that was not accessed in the last 7 days but was accessed in the last 30 days.
        # 
        # - coldDataSize: the size of cold data. Cold data is data that was not accessed in the last 30 days but was accessed in the last 90 days.
        # 
        # - freezeDataSize: the size of freeze data. Freeze data is data that was not accessed in the last 90 days.
        # 
        # - totalDataSize: the total data size.
        # 
        # - totalFileDayGrowthCount: the daily increase in the total number of files.
        # 
        # - largeFileDayGrowthCount: the daily increase in the number of large files. A large file is 1 GB or larger.
        # 
        # - mediumFileDayGrowthCount: the daily increase in the number of medium-sized files. A medium-sized file is larger than 128 MB and smaller than 1 GB.
        # 
        # - smallFileDayGrowthCount: the daily increase in the number of small files. A small file is larger than 10 MB and less than or equal to 128 MB.
        # 
        # - tinyFileDayGrowthCount: the daily increase in the number of tiny files. A tiny file is larger than 0 MB and less than or equal to 10 MB.
        # 
        # - emptyFileDayGrowthCount: the daily increase in the number of empty files. An empty file is 0 MB in size.
        # 
        # - hotDataDayGrowthSize: the daily increase in the size of hot data. Hot data is data that was accessed in the last 7 days.
        # 
        # - warmDataDayGrowthSize: the daily increase in the size of warm data. Warm data is data that was not accessed in the last 7 days but was accessed in the last 30 days.
        # 
        # - coldDataDayGrowthSize: the daily increase in the size of cold data. Cold data is data that was not accessed in the last 30 days but was accessed in the last 90 days.
        # 
        # - freezeDataDayGrowthSize: the daily increase in the size of freeze data. Freeze data is data that was not accessed in the last 90 days.
        # 
        # - totalDataDayGrowthSize: the daily increase in the total data size.
        # 
        # - totalFileCountDayGrowthRatio: the day-over-day growth ratio of the total number of files.
        # 
        # - largeFileCountDayGrowthRatio: the day-over-day growth ratio of the number of large files. A large file is 1 GB or larger.
        # 
        # - mediumFileCountDayGrowthRatio: the day-over-day growth ratio of the number of medium-sized files. A medium-sized file is larger than 128 MB and smaller than 1 GB.
        # 
        # - smallFileCountDayGrowthRatio: the day-over-day growth ratio of the number of small files. A small file is larger than 10 MB and less than or equal to 128 MB.
        # 
        # - tinyFileCountDayGrowthRatio: the day-over-day growth ratio of the number of tiny files. A tiny file is larger than 0 MB and less than or equal to 10 MB.
        # 
        # - emptyFileCountDayGrowthRatio: the day-over-day growth ratio of the number of empty files. An empty file is 0 MB in size.
        self.order_by = order_by
        # The sort order. Valid values:
        # 
        # - ASC: ascending
        # 
        # - DESC: descending
        self.order_type = order_type
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.date_time is not None:
            result['DateTime'] = self.date_time

        if self.dir_path is not None:
            result['DirPath'] = self.dir_path

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')

        if m.get('DirPath') is not None:
            self.dir_path = m.get('DirPath')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

