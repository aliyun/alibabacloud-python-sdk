# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListAppResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: List[main_models.ListAppResponseBodyData] = None,
        message: str = None,
        page_nmuber: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. This field is returned when the request fails. A successful response may not contain this field.
        self.code = code
        # The total number of application records that meet the query conditions.
        self.count = count
        # The application records on the current page.
        self.data = data
        # The error or result message. This field describes the cause when the request fails. A successful response may not contain this field.
        self.message = message
        # The page number of the current query. The name of this response field is PageNmuber.
        self.page_nmuber = page_nmuber
        # The number of records per page in the paged query.
        self.page_size = page_size
        # The unique identifier of the request. You can provide this value when troubleshooting issues.
        self.request_id = request_id
        # Indicates whether the request was processed successfully. A value of true indicates that the current request was processed successfully. To check whether an asynchronous task is completed, you must query the task status separately.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_nmuber is not None:
            result['PageNmuber'] = self.page_nmuber

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAppResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNmuber') is not None:
            self.page_nmuber = m.get('PageNmuber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAppResponseBodyData(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        app_icon_url: str = None,
        app_id: str = None,
        app_name: str = None,
        app_theme_color: str = None,
        app_type: str = None,
        biz_type: int = None,
        deletable: bool = None,
        execute_file_address: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        origin_app_type: str = None,
        os_type: str = None,
        product_type: str = None,
        silence_param: str = None,
        status: str = None,
        sub_app_type: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.ali_uid = ali_uid
        # The URL used to access the application icon.
        self.app_icon_url = app_icon_url
        # The application ID, which is used for subsequent application queries or unbinding the image.
        self.app_id = app_id
        # The display name of the application.
        self.app_name = app_name
        # The theme color saved for the application. If no theme color is specified when the application is created, #FFFFFF (white) is saved by default. The saved value is returned during a query. This field may not be configured for legacy applications.
        self.app_theme_color = app_theme_color
        # The source type of the application. Valid values:
        # 
        # - **USER_APP**: user-created application
        # - **SYS_APP**: system-provided application
        # - **VIRTUAL_APP**: virtual application
        self.app_type = app_type
        # The business type to which the application belongs. Valid values:
        # 
        # - **1**: basic product
        # - **2**: personal cloud
        # - **3**: cloud office
        # - **4**: cloud flow
        # - **10**: personal edition
        # - **20**: business edition
        # - **60**: Linggou team edition
        self.biz_type = biz_type
        # Indicates whether the current application is not referenced by any image. A value of true indicates that no image references the application. A value of false indicates that the application is still referenced by an image, and the reference must be removed before deletion.
        self.deletable = deletable
        # The path of the executable file saved when the application is created or modified. This field is returned only if the path is configured for the application. An example is the installation path of a Windows business application.
        self.execute_file_address = execute_file_address
        # The time when the application was created. The time is in ISO 8601 format, accurate to milliseconds, and the time zone offset is +00:00.
        self.gmt_create = gmt_create
        # The time when the application was last modified. The time is in ISO 8601 format, accurate to milliseconds, and the time zone offset is +00:00.
        self.gmt_modified = gmt_modified
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
        # The product to which the resource belongs. Valid values:
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
        # The command-line parameters used when the application is started.
        self.silence_param = silence_param
        # The status of the application record. The current list queries only valid and undeleted applications.
        self.status = status
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
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.app_icon_url is not None:
            result['AppIconUrl'] = self.app_icon_url

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_theme_color is not None:
            result['AppThemeColor'] = self.app_theme_color

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.deletable is not None:
            result['Deletable'] = self.deletable

        if self.execute_file_address is not None:
            result['ExecuteFileAddress'] = self.execute_file_address

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.origin_app_type is not None:
            result['OriginAppType'] = self.origin_app_type

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.silence_param is not None:
            result['SilenceParam'] = self.silence_param

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_app_type is not None:
            result['SubAppType'] = self.sub_app_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('AppIconUrl') is not None:
            self.app_icon_url = m.get('AppIconUrl')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppThemeColor') is not None:
            self.app_theme_color = m.get('AppThemeColor')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')

        if m.get('ExecuteFileAddress') is not None:
            self.execute_file_address = m.get('ExecuteFileAddress')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('OriginAppType') is not None:
            self.origin_app_type = m.get('OriginAppType')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('SilenceParam') is not None:
            self.silence_param = m.get('SilenceParam')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubAppType') is not None:
            self.sub_app_type = m.get('SubAppType')

        return self

