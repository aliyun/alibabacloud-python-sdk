# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DomainAppConfig(DaraModel):
    def __init__(
        self,
        allow_upload_custom_file_ext_list: List[str] = None,
        allow_upload_file_category_list: List[str] = None,
        same_name_file_upload_mode: str = None,
        single_file_upload_size_limit: int = None,
        web_client_download_mode: str = None,
    ):
        self.allow_upload_custom_file_ext_list = allow_upload_custom_file_ext_list
        self.allow_upload_file_category_list = allow_upload_file_category_list
        self.same_name_file_upload_mode = same_name_file_upload_mode
        self.single_file_upload_size_limit = single_file_upload_size_limit
        self.web_client_download_mode = web_client_download_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_upload_custom_file_ext_list is not None:
            result['allow_upload_custom_file_ext_list'] = self.allow_upload_custom_file_ext_list

        if self.allow_upload_file_category_list is not None:
            result['allow_upload_file_category_list'] = self.allow_upload_file_category_list

        if self.same_name_file_upload_mode is not None:
            result['same_name_file_upload_mode'] = self.same_name_file_upload_mode

        if self.single_file_upload_size_limit is not None:
            result['single_file_upload_size_limit'] = self.single_file_upload_size_limit

        if self.web_client_download_mode is not None:
            result['web_client_download_mode'] = self.web_client_download_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allow_upload_custom_file_ext_list') is not None:
            self.allow_upload_custom_file_ext_list = m.get('allow_upload_custom_file_ext_list')

        if m.get('allow_upload_file_category_list') is not None:
            self.allow_upload_file_category_list = m.get('allow_upload_file_category_list')

        if m.get('same_name_file_upload_mode') is not None:
            self.same_name_file_upload_mode = m.get('same_name_file_upload_mode')

        if m.get('single_file_upload_size_limit') is not None:
            self.single_file_upload_size_limit = m.get('single_file_upload_size_limit')

        if m.get('web_client_download_mode') is not None:
            self.web_client_download_mode = m.get('web_client_download_mode')

        return self

