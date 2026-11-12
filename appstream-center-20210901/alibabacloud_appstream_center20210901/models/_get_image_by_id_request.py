# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetImageByIdRequest(DaraModel):
    def __init__(
        self,
        biz_region_id: str = None,
        ignore_filter: bool = None,
        image_id: str = None,
        product_type: str = None,
        show_hidden: str = None,
        version_id: str = None,
    ):
        # The ID of the business region to query. If you do not specify this parameter, regions are not filtered by this parameter. The returned regions are still subject to the visibility scope of the product and the account.
        self.biz_region_id = biz_region_id
        # Specifies whether to skip the operating system and adaptation status filtering for adapted applications. Default value: false. If you set this parameter to false, only applications whose operating system matches the image and whose adaptation is complete are retained. If you set this parameter to true, these two filters are skipped. Application type filtering is still controlled by the API operation and the ShowHidden parameter.
        self.ignore_filter = ignore_filter
        # The image ID. You must specify at least one of ImageId and VersionId. If you specify only this parameter, the online version is queried.
        self.image_id = image_id
        # The product type. Examples: CloudDesktop (Cloud Desktop), CloudApp (Cloud App), and WuyingServer (WUYING Workspace Enterprise Edition workstation).
        self.product_type = product_type
        # The types of virtual applications to include in addition to the default user applications and system applications. Valid values:
        # - VIRTUAL_DESKTOP_APP: desktop virtual applications.
        # - ALL_VIRTUAL_APP: all virtual applications.
        self.show_hidden = show_hidden
        # The image version ID. You can specify this parameter alone to query a specific version. If you specify both this parameter and ImageId, the version must belong to the specified image.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.ignore_filter is not None:
            result['IgnoreFilter'] = self.ignore_filter

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.show_hidden is not None:
            result['ShowHidden'] = self.show_hidden

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('IgnoreFilter') is not None:
            self.ignore_filter = m.get('IgnoreFilter')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ShowHidden') is not None:
            self.show_hidden = m.get('ShowHidden')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

