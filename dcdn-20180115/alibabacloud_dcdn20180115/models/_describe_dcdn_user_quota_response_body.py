# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnUserQuotaResponseBody(DaraModel):
    def __init__(
        self,
        block_quota: int = None,
        block_remain: int = None,
        domain_quota: int = None,
        ignore_params_quota: int = None,
        ignore_params_remain: int = None,
        preload_quota: int = None,
        preload_remain: int = None,
        refresh_dir_quota: int = None,
        refresh_dir_remain: int = None,
        refresh_url_quota: int = None,
        refresh_url_remain: int = None,
        request_id: str = None,
    ):
        # The maximum number of URLs that can be blocked.
        self.block_quota = block_quota
        # The remaining number of URLs that can be blocked.
        self.block_remain = block_remain
        # The maximum number of accelerated domains.
        self.domain_quota = domain_quota
        # The maximum number of URLs or directories with parameters ignored that can be refreshed.
        self.ignore_params_quota = ignore_params_quota
        # The number of remaining URLs or directories with parameters ignored that can be refreshed.
        self.ignore_params_remain = ignore_params_remain
        # The maximum number of URLs that can be prefetched.
        self.preload_quota = preload_quota
        # The remaining number of URLs that can be prefetched.
        self.preload_remain = preload_remain
        # The maximum number of directories that can be refreshed.
        self.refresh_dir_quota = refresh_dir_quota
        # The remaining number of directories that can be refreshed.
        self.refresh_dir_remain = refresh_dir_remain
        # The maximum number of URLs that can be refreshed.
        self.refresh_url_quota = refresh_url_quota
        # The remaining number of URLs that can be refreshed.
        self.refresh_url_remain = refresh_url_remain
        # The ID of the request.
        self.request_id = request_id

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

        if self.domain_quota is not None:
            result['DomainQuota'] = self.domain_quota

        if self.ignore_params_quota is not None:
            result['IgnoreParamsQuota'] = self.ignore_params_quota

        if self.ignore_params_remain is not None:
            result['IgnoreParamsRemain'] = self.ignore_params_remain

        if self.preload_quota is not None:
            result['PreloadQuota'] = self.preload_quota

        if self.preload_remain is not None:
            result['PreloadRemain'] = self.preload_remain

        if self.refresh_dir_quota is not None:
            result['RefreshDirQuota'] = self.refresh_dir_quota

        if self.refresh_dir_remain is not None:
            result['RefreshDirRemain'] = self.refresh_dir_remain

        if self.refresh_url_quota is not None:
            result['RefreshUrlQuota'] = self.refresh_url_quota

        if self.refresh_url_remain is not None:
            result['RefreshUrlRemain'] = self.refresh_url_remain

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockQuota') is not None:
            self.block_quota = m.get('BlockQuota')

        if m.get('BlockRemain') is not None:
            self.block_remain = m.get('BlockRemain')

        if m.get('DomainQuota') is not None:
            self.domain_quota = m.get('DomainQuota')

        if m.get('IgnoreParamsQuota') is not None:
            self.ignore_params_quota = m.get('IgnoreParamsQuota')

        if m.get('IgnoreParamsRemain') is not None:
            self.ignore_params_remain = m.get('IgnoreParamsRemain')

        if m.get('PreloadQuota') is not None:
            self.preload_quota = m.get('PreloadQuota')

        if m.get('PreloadRemain') is not None:
            self.preload_remain = m.get('PreloadRemain')

        if m.get('RefreshDirQuota') is not None:
            self.refresh_dir_quota = m.get('RefreshDirQuota')

        if m.get('RefreshDirRemain') is not None:
            self.refresh_dir_remain = m.get('RefreshDirRemain')

        if m.get('RefreshUrlQuota') is not None:
            self.refresh_url_quota = m.get('RefreshUrlQuota')

        if m.get('RefreshUrlRemain') is not None:
            self.refresh_url_remain = m.get('RefreshUrlRemain')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

