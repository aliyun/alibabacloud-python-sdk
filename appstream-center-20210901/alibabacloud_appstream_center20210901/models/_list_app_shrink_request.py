# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAppShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_type: str = None,
        biz_type: int = None,
        biz_type_list_shrink: str = None,
        origin_app_type: str = None,
        os_type: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        product_type_list_shrink: str = None,
        sub_app_type: str = None,
    ):
        # The application ID for exact query. If this parameter is omitted, applications are not filtered by application ID.
        self.app_id = app_id
        # The application name filter. Contains matching is supported.
        self.app_name = app_name
        # The source type of the application. Valid values:
        # 
        # - **USER_APP**: User-created applications.
        # - **SYS_APP**: System-provided applications.
        # - **VIRTUAL_APP**: Virtual applications.
        self.app_type = app_type
        # Filters by a single business type. If specified together with BizTypeList, the intersection is used. Valid values:
        # 
        # - **1**: Basic products.
        # - **2**: Personal cloud.
        # - **3**: Cloud office.
        # - **4**: Cloud Flow.
        # - **10**: Personal Edition.
        # - **20**: Business Edition.
        # - **60**: Linggou Team Edition.
        self.biz_type = biz_type
        # The list of business types for filtering. A match with any business type in the list is considered a match. If specified together with BizType, the single-value condition must still be met.
        self.biz_type_list_shrink = biz_type_list_shrink
        # The form of the application. Valid values:
        # 
        # - **CLIENT_BASE**: Client applications.
        # - **WEB_BASE**: Browser applications.
        # - **CLOUD_NATIVE_BASE**: Cloud-native applications.
        # - **PORT_SERVICE_BASE**: Port service applications.
        # - **AGENT_SERVICE_BASE**: Agent applications.
        self.origin_app_type = origin_app_type
        # The type of operating system used by the application. Valid values:
        # 
        # - **Unknown**: The operating system is unknown.
        # - **Windows**: Windows operating system.
        # - **Linux**: Linux operating system.
        # - **Android**: Android operating system.
        self.os_type = os_type
        # The page number for the query. Start from 1. If this parameter is omitted, set to 0, or set to 1, the first page is queried.
        self.page_number = page_number
        # The number of records to return on each page. If this parameter is omitted or set to a value less than 1, the value 10 is used.
        self.page_size = page_size
        # Filters by a single associated product. If specified together with ProductTypeList, the intersection is used. Valid values:
        # 
        # - **CloudGame**: Cloud game.
        # - **CloudApp**: Wuying cloud application.
        # - **CloudBrowser**: Secure browser.
        # - **CloudDesktop**: Wuying cloud desktop.
        # - **ImageBuilder**: Image builder resources.
        # - **ImageValidate**: Image validation resources.
        # - **AndroidCloud**: Android cloud.
        # - **GpuRender**: GPU rendering.
        # - **AndroidGpuRender**: Android cloud GPU rendering.
        # - **WuyingServer**: Enterprise Edition workstation.
        # - **GpuProxy**: GPU remote rendering proxy.
        # - **GpuCache**: GPU remote rendering cache.
        # - **AIAgent**: AI Agent service.
        # - **HostedDesktop**: Hosted desktop.
        # - **WuyingWorkstation**: Personal Edition container workstation.
        # - **WuyingWorkstationBusiness**: Business Edition container workstation.
        # - **WuyingWorkstationTeam**: Linggou Team Edition container workstation.
        self.product_type = product_type
        # The list of associated products for filtering. A match with any product in the list is considered a match. If specified together with ProductType, the single-value condition must still be met.
        self.product_type_list_shrink = product_type_list_shrink
        # The subtype of the application. Valid values:
        # 
        # - **PWA**: Progressive web applications.
        # - **SAAS**: Software as a Service (SaaS) applications.
        # - **SANDBOX**: Sandbox applications.
        # - **CONTAINER**: Container applications.
        self.sub_app_type = sub_app_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.biz_type_list_shrink is not None:
            result['BizTypeList'] = self.biz_type_list_shrink

        if self.origin_app_type is not None:
            result['OriginAppType'] = self.origin_app_type

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.product_type_list_shrink is not None:
            result['ProductTypeList'] = self.product_type_list_shrink

        if self.sub_app_type is not None:
            result['SubAppType'] = self.sub_app_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('BizTypeList') is not None:
            self.biz_type_list_shrink = m.get('BizTypeList')

        if m.get('OriginAppType') is not None:
            self.origin_app_type = m.get('OriginAppType')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ProductTypeList') is not None:
            self.product_type_list_shrink = m.get('ProductTypeList')

        if m.get('SubAppType') is not None:
            self.sub_app_type = m.get('SubAppType')

        return self

