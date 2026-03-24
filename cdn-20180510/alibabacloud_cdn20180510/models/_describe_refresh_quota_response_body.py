# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRefreshQuotaResponseBody(DaraModel):
    def __init__(
        self,
        block_quota: str = None,
        block_remain: str = None,
        dir_quota: str = None,
        dir_remain: str = None,
        ignore_params_quota: str = None,
        ignore_params_remain: str = None,
        preload_edge_quota: str = None,
        preload_edge_remain: str = None,
        preload_quota: str = None,
        preload_remain: str = None,
        regex_quota: str = None,
        regex_remain: str = None,
        request_id: str = None,
        url_quota: str = None,
        url_remain: str = None,
    ):
        # The maximum number of URLs that can be refreshed on the current day.
        self.block_quota = block_quota
        # The remaining number of times that you can prefetch content to L2 points of presence (POPs) on the current day.
        self.block_remain = block_remain
        # The ID of the request.
        self.dir_quota = dir_quota
        # The remaining number of URLs that can be refreshed on the current day.
        self.dir_remain = dir_remain
        # The maximum number of URLs or directories with parameters ignored that can be refreshed on the current day.
        self.ignore_params_quota = ignore_params_quota
        # The number of remaining URLs or directories that can be refreshed with parameters ignored on the current day.
        self.ignore_params_remain = ignore_params_remain
        # The maximum number of directories that can be refreshed on the current day.
        self.preload_edge_quota = preload_edge_quota
        # The maximum number of times that you can prefetch content to L1 POPs on the current day.
        self.preload_edge_remain = preload_edge_remain
        # The remaining number of times that you can prefetch content to L1 POPs on the current day.
        self.preload_quota = preload_quota
        # The maximum number of times that you can prefetch content to L1 nodes on the current day.
        self.preload_remain = preload_remain
        # The maximum number of times that you can prefetch content to L2 POPs on the current day.
        self.regex_quota = regex_quota
        # The remaining number of URLs that can be blocked on the current day.
        self.regex_remain = regex_remain
        # The maximum number of URLs and directories that can be blocked on the current day.
        self.request_id = request_id
        # The remaining number of directories that can be refreshed on the current day.
        self.url_quota = url_quota
        # The remaining number of URLs or directories that can be refreshed by using regular expressions on the current day.
        self.url_remain = url_remain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_quota is not None:
            result['BlockQuota'] = self.block_quota

        if self.block_remain is not None:
            result['BlockRemain'] = self.block_remain

        if self.dir_quota is not None:
            result['DirQuota'] = self.dir_quota

        if self.dir_remain is not None:
            result['DirRemain'] = self.dir_remain

        if self.ignore_params_quota is not None:
            result['IgnoreParamsQuota'] = self.ignore_params_quota

        if self.ignore_params_remain is not None:
            result['IgnoreParamsRemain'] = self.ignore_params_remain

        if self.preload_edge_quota is not None:
            result['PreloadEdgeQuota'] = self.preload_edge_quota

        if self.preload_edge_remain is not None:
            result['PreloadEdgeRemain'] = self.preload_edge_remain

        if self.preload_quota is not None:
            result['PreloadQuota'] = self.preload_quota

        if self.preload_remain is not None:
            result['PreloadRemain'] = self.preload_remain

        if self.regex_quota is not None:
            result['RegexQuota'] = self.regex_quota

        if self.regex_remain is not None:
            result['RegexRemain'] = self.regex_remain

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.url_quota is not None:
            result['UrlQuota'] = self.url_quota

        if self.url_remain is not None:
            result['UrlRemain'] = self.url_remain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockQuota') is not None:
            self.block_quota = m.get('BlockQuota')

        if m.get('BlockRemain') is not None:
            self.block_remain = m.get('BlockRemain')

        if m.get('DirQuota') is not None:
            self.dir_quota = m.get('DirQuota')

        if m.get('DirRemain') is not None:
            self.dir_remain = m.get('DirRemain')

        if m.get('IgnoreParamsQuota') is not None:
            self.ignore_params_quota = m.get('IgnoreParamsQuota')

        if m.get('IgnoreParamsRemain') is not None:
            self.ignore_params_remain = m.get('IgnoreParamsRemain')

        if m.get('PreloadEdgeQuota') is not None:
            self.preload_edge_quota = m.get('PreloadEdgeQuota')

        if m.get('PreloadEdgeRemain') is not None:
            self.preload_edge_remain = m.get('PreloadEdgeRemain')

        if m.get('PreloadQuota') is not None:
            self.preload_quota = m.get('PreloadQuota')

        if m.get('PreloadRemain') is not None:
            self.preload_remain = m.get('PreloadRemain')

        if m.get('RegexQuota') is not None:
            self.regex_quota = m.get('RegexQuota')

        if m.get('RegexRemain') is not None:
            self.regex_remain = m.get('RegexRemain')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UrlQuota') is not None:
            self.url_quota = m.get('UrlQuota')

        if m.get('UrlRemain') is not None:
            self.url_remain = m.get('UrlRemain')

        return self

