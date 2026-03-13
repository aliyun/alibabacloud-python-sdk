# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribeComponentAssetsResponseBody(DaraModel):
    def __init__(
        self,
        component_assets: List[main_models.DescribeComponentAssetsResponseBodyComponentAssets] = None,
        request_id: str = None,
    ):
        # The information about the assets.
        self.component_assets = component_assets
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.component_assets:
            for v1 in self.component_assets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ComponentAssets'] = []
        if self.component_assets is not None:
            for k1 in self.component_assets:
                result['ComponentAssets'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.component_assets = []
        if m.get('ComponentAssets') is not None:
            for k1 in m.get('ComponentAssets'):
                temp_model = main_models.DescribeComponentAssetsResponseBodyComponentAssets()
                self.component_assets.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeComponentAssetsResponseBodyComponentAssets(DaraModel):
    def __init__(
        self,
        asset_uuid: str = None,
        componentname: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        params: str = None,
    ):
        # The UUID of the asset.
        self.asset_uuid = asset_uuid
        # The name of the component to which the asset belongs.
        self.componentname = componentname
        # The time when the asset was created. The time is in the yyyy-MM-ddTHH:mm:ssZ format and is displayed in UTC.
        self.gmt_create = gmt_create
        # The time when the asset was modified. The time is in the yyyy-MM-ddTHH:mm:ssZ format and is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The UUID of the asset.
        self.id = id
        # The name of the asset.
        self.name = name
        # The configurations of the asset in the JSON string format. DescribeComponentAssetForm
        # 
        # >  For more information, see [DescribeComponentAssetForm](~~DescribeComponentAssetForm~~).
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_uuid is not None:
            result['AssetUuid'] = self.asset_uuid

        if self.componentname is not None:
            result['Componentname'] = self.componentname

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.params is not None:
            result['Params'] = self.params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetUuid') is not None:
            self.asset_uuid = m.get('AssetUuid')

        if m.get('Componentname') is not None:
            self.componentname = m.get('Componentname')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        return self

