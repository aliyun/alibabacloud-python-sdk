# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class AddVirusScanAdditionalListsRequest(DaraModel):
    def __init__(
        self,
        additional_lists: List[main_models.AddVirusScanAdditionalListsRequestAdditionalLists] = None,
        dev_type: str = None,
    ):
        # The list of entries to add. The list must contain at least one entry.
        self.additional_lists = additional_lists
        # The operating system type to which the list applies. Valid values:
        # - **windows**: Windows.
        # - **macOS**: macOS.
        # 
        # This parameter is required.
        self.dev_type = dev_type

    def validate(self):
        if self.additional_lists:
            for v1 in self.additional_lists:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdditionalLists'] = []
        if self.additional_lists is not None:
            for k1 in self.additional_lists:
                result['AdditionalLists'].append(k1.to_map() if k1 else None)

        if self.dev_type is not None:
            result['DevType'] = self.dev_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.additional_lists = []
        if m.get('AdditionalLists') is not None:
            for k1 in m.get('AdditionalLists'):
                temp_model = main_models.AddVirusScanAdditionalListsRequestAdditionalLists()
                self.additional_lists.append(temp_model.from_map(k1))

        if m.get('DevType') is not None:
            self.dev_type = m.get('DevType')

        return self

class AddVirusScanAdditionalListsRequestAdditionalLists(DaraModel):
    def __init__(
        self,
        additional_type: str = None,
        detail: str = None,
        list_type: str = None,
    ):
        # The matching dimension of the list entry. Valid values:
        # - **FileSuffix**: Matches by file name extension.
        # - **FileName**: Matches by file name.
        # - **FolderName**: Matches by folder name.
        # - **FilePath**: Matches by file path.
        # - **FileMd5**: Matches by file MD5 hash.
        self.additional_type = additional_type
        # The content of the list entry. The value can be up to 255 characters in length. The meaning of this parameter is determined by the AdditionalType parameter. If AdditionalType is set to FileSuffix, specify the file name extension. If AdditionalType is set to FileName, specify the file name. If AdditionalType is set to FolderName, specify the folder name. If AdditionalType is set to FilePath, specify the file path. If AdditionalType is set to FileMd5, specify the MD5 hash of the file.
        self.detail = detail
        # The list type. Valid values:
        # - **Blacklist**: Blacklist. Matched files are directly identified as virus files.
        # - **Whitelist**: Whitelist. Matched files are excluded from virus detection.
        self.list_type = list_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_type is not None:
            result['AdditionalType'] = self.additional_type

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.list_type is not None:
            result['ListType'] = self.list_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalType') is not None:
            self.additional_type = m.get('AdditionalType')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')

        return self

