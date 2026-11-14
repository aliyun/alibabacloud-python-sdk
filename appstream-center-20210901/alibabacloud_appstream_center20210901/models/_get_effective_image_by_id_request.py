# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEffectiveImageByIdRequest(DaraModel):
    def __init__(
        self,
        biz_region_id: str = None,
        content_locale: str = None,
        ignore_filter: bool = None,
        image_id: str = None,
        image_type: str = None,
        product_type: str = None,
        show_hidden: str = None,
    ):
        # The ID of the business region to query. If this parameter is not specified, regions are not filtered by this parameter. The returned regions are still constrained by the product type and the visible scope of the account.
        self.biz_region_id = biz_region_id
        # The content language of the community image documentation in BCP 47 format, such as zh-CN and en-US. Default value: zh-CN.
        self.content_locale = content_locale
        # Specifies whether to skip filtering based on the operating system and adaptation status of adapted applications. Default value: false. A value of false retains only applications that match the image operating system and have completed adaptation. A value of true skips these two filters. Application type filtering is still controlled by the API operation and the ShowHidden parameter.
        self.ignore_filter = ignore_filter
        # The image ID. This parameter is required when querying effective versions.
        self.image_id = image_id
        # The image type. Valid values:
        # - System: system images.
        # - User: custom images.
        # - Shared: shared images.
        # - Community: community images.
        self.image_type = image_type
        # The product type, such as CloudDesktop (Cloud Desktop), CloudApp (Cloud App), and WuyingServer (workstation).
        self.product_type = product_type
        # Specifies the additional virtual application types to include in the response besides the default user and system applications. Valid values:
        # - VIRTUAL_DESKTOP_APP: desktop virtual applications.
        # - ALL_VIRTUAL_APP: all virtual applications.
        self.show_hidden = show_hidden

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.content_locale is not None:
            result['ContentLocale'] = self.content_locale

        if self.ignore_filter is not None:
            result['IgnoreFilter'] = self.ignore_filter

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.show_hidden is not None:
            result['ShowHidden'] = self.show_hidden

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ContentLocale') is not None:
            self.content_locale = m.get('ContentLocale')

        if m.get('IgnoreFilter') is not None:
            self.ignore_filter = m.get('IgnoreFilter')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ShowHidden') is not None:
            self.show_hidden = m.get('ShowHidden')

        return self

