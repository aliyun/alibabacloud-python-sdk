# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAvailableImagesShrinkRequest(DaraModel):
    def __init__(
        self,
        directory_service_shrink: str = None,
        enable_ht: bool = None,
        hpcinter_connect: str = None,
        image_owner_alias: str = None,
        instance_type: str = None,
        is_public: bool = None,
        page_number: int = None,
        page_size: int = None,
        scheduler_shrink: str = None,
    ):
        # The information about the domain account service.
        self.directory_service_shrink = directory_service_shrink
        # Specifies whether to return images in which hyper-threading is enabled.
        self.enable_ht = enable_ht
        # The network type of the images that you want to query.
        self.hpcinter_connect = hpcinter_connect
        # The image source. Valid values:
        # 
        # *   system: system image.
        # *   self: custom image.
        # *   others: shared image.
        self.image_owner_alias = image_owner_alias
        # The instance type.
        # 
        # >  By default, if you do not specify an instance type, the list of images that are supported by all instance types are queried. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        self.instance_type = instance_type
        # Specifies whether to return published community images. Valid values:
        # 
        # *   true: returns published community images. If you set the value of this parameter to `true`, the `ImageOwnerAlias` parameter must be set to `others`.
        # *   false: returns non-community images. The value of the `ImageOwnerAlias` parameter prevails.
        # 
        # Default value: false.
        self.is_public = is_public
        # The page number of the page to return.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 50. Default value: 10.
        self.page_size = page_size
        # The scheduler information about the images that you want to query.
        self.scheduler_shrink = scheduler_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_service_shrink is not None:
            result['DirectoryService'] = self.directory_service_shrink

        if self.enable_ht is not None:
            result['EnableHT'] = self.enable_ht

        if self.hpcinter_connect is not None:
            result['HPCInterConnect'] = self.hpcinter_connect

        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.is_public is not None:
            result['IsPublic'] = self.is_public

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.scheduler_shrink is not None:
            result['Scheduler'] = self.scheduler_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryService') is not None:
            self.directory_service_shrink = m.get('DirectoryService')

        if m.get('EnableHT') is not None:
            self.enable_ht = m.get('EnableHT')

        if m.get('HPCInterConnect') is not None:
            self.hpcinter_connect = m.get('HPCInterConnect')

        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IsPublic') is not None:
            self.is_public = m.get('IsPublic')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Scheduler') is not None:
            self.scheduler_shrink = m.get('Scheduler')

        return self

