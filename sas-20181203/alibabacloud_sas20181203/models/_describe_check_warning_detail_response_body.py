# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeCheckWarningDetailResponseBody(DaraModel):
    def __init__(
        self,
        advice: str = None,
        check_detail_asset_info: List[Dict[str, str]] = None,
        check_detail_columns: List[main_models.DescribeCheckWarningDetailResponseBodyCheckDetailColumns] = None,
        check_id: int = None,
        description: str = None,
        item: str = None,
        level: str = None,
        prompt: str = None,
        request_id: str = None,
        type: str = None,
    ):
        # The suggestion for the management of the risk item.
        self.advice = advice
        # List of asset details to check.
        self.check_detail_asset_info = check_detail_asset_info
        # Detection content details.
        self.check_detail_columns = check_detail_columns
        # The ID of the check item.
        self.check_id = check_id
        # The additional information about the risk item.
        self.description = description
        # The name of the check item.
        self.item = item
        # The risk level of the check item. Valid values:
        # 
        # *   **high**: The item is a high-risk item and is highlighted in red.
        # *   **medium**: The item is a medium-risk item and is highlighted in orange.
        # *   **low**: The item is a low-risk item and is highlighted in gray.
        self.level = level
        # The prompt for the risk item.
        self.prompt = prompt
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The type of the check item. Valid values:
        # 
        # *   **hc_exploit**: unauthorized access
        # *   **hc_djbh**: classified protection compliance
        # *   **hc_best_secruity**: best security practice
        # *   **hc_container**: container security
        # *   **hc_custom**: custom baseline
        # *   **cis**: Center for Internet Security (CIS) compliance
        # *   **weak_password**: weak password
        self.type = type

    def validate(self):
        if self.check_detail_columns:
            for v1 in self.check_detail_columns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advice is not None:
            result['Advice'] = self.advice

        if self.check_detail_asset_info is not None:
            result['CheckDetailAssetInfo'] = self.check_detail_asset_info

        result['CheckDetailColumns'] = []
        if self.check_detail_columns is not None:
            for k1 in self.check_detail_columns:
                result['CheckDetailColumns'].append(k1.to_map() if k1 else None)

        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.description is not None:
            result['Description'] = self.description

        if self.item is not None:
            result['Item'] = self.item

        if self.level is not None:
            result['Level'] = self.level

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')

        if m.get('CheckDetailAssetInfo') is not None:
            self.check_detail_asset_info = m.get('CheckDetailAssetInfo')

        self.check_detail_columns = []
        if m.get('CheckDetailColumns') is not None:
            for k1 in m.get('CheckDetailColumns'):
                temp_model = main_models.DescribeCheckWarningDetailResponseBodyCheckDetailColumns()
                self.check_detail_columns.append(temp_model.from_map(k1))

        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Item') is not None:
            self.item = m.get('Item')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeCheckWarningDetailResponseBodyCheckDetailColumns(DaraModel):
    def __init__(
        self,
        grids: List[main_models.DescribeCheckWarningDetailResponseBodyCheckDetailColumnsGrids] = None,
        key: str = None,
        show_name: str = None,
        type: str = None,
    ):
        # Detection content list.
        self.grids = grids
        # Key to detect content.
        self.key = key
        # The detection content key corresponds to the display name.
        self.show_name = show_name
        # Display type. Value:
        # - **grid**: Detection grid
        # - **text**: text
        self.type = type

    def validate(self):
        if self.grids:
            for v1 in self.grids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Grids'] = []
        if self.grids is not None:
            for k1 in self.grids:
                result['Grids'].append(k1.to_map() if k1 else None)

        if self.key is not None:
            result['Key'] = self.key

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.grids = []
        if m.get('Grids') is not None:
            for k1 in m.get('Grids'):
                temp_model = main_models.DescribeCheckWarningDetailResponseBodyCheckDetailColumnsGrids()
                self.grids.append(temp_model.from_map(k1))

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeCheckWarningDetailResponseBodyCheckDetailColumnsGrids(DaraModel):
    def __init__(
        self,
        key: str = None,
        show_name: str = None,
        type: str = None,
    ):
        # Key to detect content.
        self.key = key
        # The detection content key corresponds to the display name.
        self.show_name = show_name
        # Display type. Value:
        # - **grid**: Detection grid
        # - **text**: text
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

