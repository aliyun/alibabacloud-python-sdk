# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVodRefreshQuotaResponseBody(DaraModel):
    def __init__(
        self,
        block_quota: str = None,
        dir_quota: str = None,
        dir_remain: str = None,
        preload_quota: str = None,
        preload_remain: str = None,
        request_id: str = None,
        url_quota: str = None,
        url_remain: str = None,
        block_remain: str = None,
    ):
        # The maximum number of Object Storage Service (OSS) buckets that can be refreshed each day.
        self.block_quota = block_quota
        # The maximum number of directories of files that can be refreshed each day.
        self.dir_quota = dir_quota
        # The remaining number of directories of files that can be refreshed on the current day.
        self.dir_remain = dir_remain
        # The maximum number of URLs of files that can be prefetched each day.
        self.preload_quota = preload_quota
        # The remaining number of URLs of files that can be prefetched on the current day.
        self.preload_remain = preload_remain
        # The ID of the request.
        self.request_id = request_id
        # The maximum number of URLs of files that can be refreshed each day.
        self.url_quota = url_quota
        # The remaining number of URLs of files that can be refreshed on the current day.
        self.url_remain = url_remain
        # The remaining number of OSS buckets that can be refreshed on the current day.
        self.block_remain = block_remain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_quota is not None:
            result['BlockQuota'] = self.block_quota

        if self.dir_quota is not None:
            result['DirQuota'] = self.dir_quota

        if self.dir_remain is not None:
            result['DirRemain'] = self.dir_remain

        if self.preload_quota is not None:
            result['PreloadQuota'] = self.preload_quota

        if self.preload_remain is not None:
            result['PreloadRemain'] = self.preload_remain

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.url_quota is not None:
            result['UrlQuota'] = self.url_quota

        if self.url_remain is not None:
            result['UrlRemain'] = self.url_remain

        if self.block_remain is not None:
            result['blockRemain'] = self.block_remain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockQuota') is not None:
            self.block_quota = m.get('BlockQuota')

        if m.get('DirQuota') is not None:
            self.dir_quota = m.get('DirQuota')

        if m.get('DirRemain') is not None:
            self.dir_remain = m.get('DirRemain')

        if m.get('PreloadQuota') is not None:
            self.preload_quota = m.get('PreloadQuota')

        if m.get('PreloadRemain') is not None:
            self.preload_remain = m.get('PreloadRemain')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UrlQuota') is not None:
            self.url_quota = m.get('UrlQuota')

        if m.get('UrlRemain') is not None:
            self.url_remain = m.get('UrlRemain')

        if m.get('blockRemain') is not None:
            self.block_remain = m.get('blockRemain')

        return self

