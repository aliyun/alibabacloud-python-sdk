# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateProductVersionRequest(DaraModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        guidance: str = None,
        product_version_id: str = None,
        product_version_name: str = None,
    ):
        # Specifies whether to enable the product version. Valid values:
        # 
        # *   true: enables the product version. This is the default value.
        # *   false: disables the product version.
        self.active = active
        # The description of the product version.
        # 
        # The value must be 1 to 128 characters in length.
        self.description = description
        # The recommendation information. Valid values:
        # 
        # *   Default: No recommendation information is provided. This is the default value.
        # *   Recommended: the recommended version.
        # *   Latest: the latest version.
        # *   Deprecated: the version that is about to be discontinued.
        self.guidance = guidance
        # The ID of the product version.
        # 
        # This parameter is required.
        self.product_version_id = product_version_id
        # The name of the product version.
        # 
        # The value must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.product_version_name = product_version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.description is not None:
            result['Description'] = self.description

        if self.guidance is not None:
            result['Guidance'] = self.guidance

        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id

        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Guidance') is not None:
            self.guidance = m.get('Guidance')

        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')

        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')

        return self

