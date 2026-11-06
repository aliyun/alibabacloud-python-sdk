# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAppRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_type: str = None,
        biz_type: int = None,
        biz_type_list: List[int] = None,
        origin_app_type: str = None,
        os_type: str = None,
        page_number: int = None,
        page_size: int = None,
        product_type: str = None,
        product_type_list: List[str] = None,
        sub_app_type: str = None,
    ):
        # Specifies the application ID for exact match. If omitted, applications are not filtered by application ID.
        self.app_id = app_id
        # The application name used to filter applications. Partial match is supported.
        self.app_name = app_name
        # The source type of the application. Valid values:
        # 
        # - **USER_APP**: user-created application
        # - **SYS_APP**: system-provided application
        # - **VIRTUAL_APP**: virtual application
        self.app_type = app_type
        # Filters by a single business type. If specified simultaneously with BizTypeList, the intersection is used. Valid values:
        # 
        # - **1**: basic product
        # - **2**: personal cloud
        # - **3**: cloud office
        # - **4**: cloud flow
        # - **10**: personal edition
        # - **20**: business edition
        # - **60**: Linggou team edition
        self.biz_type = biz_type
        # The list of business types used to filter applications. An application is matched if it matches any business type in the list. If specified simultaneously with BizType, the single-value condition must still be met.
        self.biz_type_list = biz_type_list
        # The form of the application. Valid values:
        # 
        # - **CLIENT_BASE**: client application
        # - **WEB_BASE**: browser application
        # - **CLOUD_NATIVE_BASE**: cloud-native application
        # - **PORT_SERVICE_BASE**: port service application
        # - **AGENT_SERVICE_BASE**: agent application
        self.origin_app_type = origin_app_type
        # The type of the operating system used by the application. Valid values:
        # 
        # - **Unknown**: unknown operating system
        # - **Windows**: Windows operating system
        # - **Linux**: Linux operating system
        # - **Android**: Android operating system
        self.os_type = os_type
        # The page number for the query. Query pages starting from 1. If omitted, set to 0, or set to 1, the first page is queried.
        self.page_number = page_number
        # The number of records returned per page. If omitted or set to a value less than 1, the value is processed as 10.
        self.page_size = page_size
        # Filters by a single associated product. If specified simultaneously with ProductTypeList, the intersection is used. Valid values:
        # 
        # - **CloudGame**: cloud game
        # - **CloudApp**: Wuying cloud application
        # - **CloudBrowser**: secure browser
        # - **CloudDesktop**: Wuying cloud computer
        # - **ImageBuilder**: image building resource
        # - **ImageValidate**: image validation resource
        # - **AndroidCloud**: Android cloud
        # - **GpuRender**: GPU rendering
        # - **AndroidGpuRender**: Android cloud GPU rendering
        # - **WuyingServer**: enterprise edition workstation
        # - **GpuProxy**: GPU remote rendering proxy
        # - **GpuCache**: GPU remote rendering cache
        # - **AIAgent**: AI agent service
        # - **HostedDesktop**: hosted computer
        # - **WuyingWorkstation**: personal edition container workstation
        # - **WuyingWorkstationBusiness**: business edition container workstation
        # - **WuyingWorkstationTeam**: Linggou team edition container workstation
        self.product_type = product_type
        # The list of associated products used to filter applications. An application is matched if it matches any product in the list. If specified simultaneously with ProductType, the single-value condition must still be met.
        self.product_type_list = product_type_list
        # The subtype of the application. Valid values:
        # 
        # - **PWA**: progressive web application
        # - **SAAS**: software as a service (SaaS) application
        # - **SANDBOX**: sandbox application
        # - **CONTAINER**: container application
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

        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list

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

        if self.product_type_list is not None:
            result['ProductTypeList'] = self.product_type_list

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
            self.biz_type_list = m.get('BizTypeList')

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
            self.product_type_list = m.get('ProductTypeList')

        if m.get('SubAppType') is not None:
            self.sub_app_type = m.get('SubAppType')

        return self

