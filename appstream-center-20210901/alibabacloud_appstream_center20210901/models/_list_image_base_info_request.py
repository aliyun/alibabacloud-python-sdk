# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListImageBaseInfoRequest(DaraModel):
    def __init__(
        self,
        biz_type: int = None,
        image_id: str = None,
        image_name: str = None,
        image_type: str = None,
        os_type: str = None,
        package_type: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        protocol_type: str = None,
        status: str = None,
    ):
        # The business line code. Default value: 1.
        self.biz_type = biz_type
        # The image ID. You can specify multiple IDs separated by commas (,). The query matches any of the specified IDs.
        self.image_id = image_id
        # The image query keyword. Fuzzy matching is performed on both the image name and the image ID.
        self.image_name = image_name
        # The image type. Valid values: System (system image), User (custom image), Shared (shared image), and Community (community image).
        self.image_type = image_type
        # The image operating system type. Valid values: Windows (Windows operating system), Linux (Linux operating system), Android (Android operating system), and Unknown (unknown operating system).
        self.os_type = os_type
        # The image package type. Valid values: Ecs (ECS image), Vhd (VHD image), Container (container image), Ecs_Container (ECS and container composite image), and K8s_Node (Kubernetes node image).
        self.package_type = package_type
        # The page number. Pages start from page 1. If you do not specify this parameter or specify a value less than 1, the first page is returned.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10. Maximum value: 100. If the value is less than 1, 10 entries are returned. If the value is greater than 100, 100 entries are returned.
        self.page_size = page_size
        # The product type, which is used to filter the products to which the images belong. Examples: CloudDesktop (WUYING Workspace), CloudApp (WUYING Cloud App), and WuyingServer (WUYING Workstation).
        self.product_type = product_type
        # The image protocol type. Valid values: ASP (Alibaba Cloud self-developed ASP protocol) and HDX (HDX protocol).
        self.protocol_type = protocol_type
        # The image status. Valid values: INIT (initialization), CREATING (creating), AVAILABLE (available), and CREATE_FAILED (creation failed). If you do not specify this parameter, all non-deleted images are queried. Deleted images are not returned.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

