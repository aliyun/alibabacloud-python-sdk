# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20210602 import models as main_models
from darabonba.model import DaraModel

class ListTenantAppResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListTenantAppResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The business result code, returned as a string. The value is typically "200" when the request is successful.
        self.code = code
        # The list of applications on the current page. Each element represents an application.
        self.data = data
        # The HTTP status code field in the business response. This field may be empty. The actual transmission status is determined by the HTTP response status.
        self.http_status_code = http_status_code
        # The description of the request processing result.
        self.message = message
        # The actual page number of the query.
        self.page_number = page_number
        # The actual number of entries per page.
        self.page_size = page_size
        # The request tracking ID. Provide this value when reporting issues.
        self.request_id = request_id
        # Indicates whether the request was processed successfully. Valid values:
        # - true: Succeeded.
        # - false: Failed.
        # 
        # Refer to the corresponding field descriptions for specific business meanings.
        self.success = success
        # The total number of applications that match the filter conditions. This value is not equal to the length of the array on the current page.
        self.total_count = total_count

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

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListTenantAppResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTenantAppResponseBodyData(DaraModel):
    def __init__(
        self,
        admin_tag: List[str] = None,
        app_admin_tag: str = None,
        app_reg_info: str = None,
        app_tag: List[str] = None,
        app_uid: str = None,
        auth_type: str = None,
        auto_delete_flag: bool = None,
        auto_install_flag: bool = None,
        auto_install_type: str = None,
        auto_installment_type: int = None,
        cate_id: int = None,
        cate_name: str = None,
        cluster_uid: str = None,
        description: str = None,
        developer: str = None,
        discount_price: float = None,
        distribute_type: str = None,
        expire_time: str = None,
        extend: str = None,
        file_name: str = None,
        file_path: str = None,
        file_real_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        has_cert: bool = None,
        icon_url: str = None,
        icon_url_internal: str = None,
        id: int = None,
        install: bool = None,
        install_mode: int = None,
        is_admin: bool = None,
        is_free: str = None,
        is_game: bool = None,
        is_white_list: int = None,
        item_code: str = None,
        labels: str = None,
        license_type: str = None,
        manage_cate_en_name: str = None,
        manage_cate_id: int = None,
        manage_cate_name: str = None,
        name: str = None,
        origin_app_type: str = None,
        original_price: float = None,
        os_type: str = None,
        owner_os: str = None,
        payment_type: int = None,
        price: str = None,
        priority: int = None,
        publish_date: str = None,
        publish_type: str = None,
        sandbox_mode: int = None,
        search_tag: str = None,
        silence_delete_flag: int = None,
        silence_delete_param: str = None,
        silence_flag: int = None,
        silence_param: str = None,
        size: int = None,
        source_type: str = None,
        start_time: str = None,
        status: str = None,
        sub_app_type: str = None,
        sub_source_type: str = None,
        subscribe_count: int = None,
        supplier_id: int = None,
        user_tag: List[str] = None,
        version: str = None,
        version_name: str = None,
        wam_file_name: str = None,
        wam_file_path: str = None,
        wam_file_real_name: str = None,
        wam_file_size: int = None,
    ):
        # An internal field. We do not recommend that you use this field.
        self.admin_tag = admin_tag
        # An internal field. We do not recommend that you use this field.
        self.app_admin_tag = app_admin_tag
        # The application registry identification information, returned as a string. This value can be used to match the name of an application registry entry.
        self.app_reg_info = app_reg_info
        # An internal field. We do not recommend that you use this field.
        self.app_tag = app_tag
        # The application UID string, which is a different identifier from the numeric Id field.
        self.app_uid = app_uid
        # The authorization dimension of the application.
        # 
        # Valid values:
        # - auth_type_user: Authorized by user.
        # - auth_type_resource_group: Authorized by resource group.
        self.auth_type = auth_type
        # **[Deprecated]**
        self.auto_delete_flag = auto_delete_flag
        # **[Deprecated]**
        self.auto_install_flag = auto_install_flag
        # **[Deprecated]**
        self.auto_install_type = auto_install_type
        # The new automatic installation scope policy. Use this field together with AuthType to determine the authorization dimension. Valid values:
        # - 0: Automatically install for all visible users or resource groups.
        # - 1: Automatically install for some visible users or resource groups.
        # - 2: Disable automatic installation.
        # - 99: Unknown policy.
        # 
        # This field describes the configuration scope and does not indicate that the installation has been completed on the endpoint.
        self.auto_installment_type = auto_installment_type
        # The display category ID of the application. The category ID is a dynamic identifier and is not a fixed enumeration.
        self.cate_id = cate_id
        # The display category name of the application.
        self.cate_name = cate_name
        # **[Deprecated]**
        self.cluster_uid = cluster_uid
        # The description of the application.
        self.description = description
        # The name of the application developer.
        self.developer = developer
        # **[Deprecated]**
        self.discount_price = discount_price
        # The authorization distribution scope of the application. This field must be interpreted together with AuthType. An empty value does not necessarily mean that the application is not distributed.
        # 
        # Valid values:
        # - ALL: Distributed to all.
        # - DESIGNATED: Distributed to a specified scope.
        # - NOTDISTRO: Not distributed.
        # - UNKNOWN: Unknown scope.
        # 
        # The distribution target is determined by AuthType.
        self.distribute_type = distribute_type
        # The authorization end time of the application. The value is returned as a string with a time zone, in the format of date, the letter T, hours-minutes-seconds, 3-digit milliseconds, and a time zone offset without colons. The +0000 in the example indicates UTC. This field may be empty or not returned if no value is available.
        self.expire_time = expire_time
        # The extended information of the application, returned as a string. There is no unified fixed field structure.
        self.extend = extend
        # The storage file name of the installation package, which may differ from the original file name.
        self.file_name = file_name
        # The storage path of the installation package. This value is not a directly accessible download URL.
        self.file_path = file_path
        # The original file name of the installation package.
        self.file_real_name = file_real_name
        # The creation time of the application record. The value is returned as a string with a time zone, in the format of date, the letter T, hours-minutes-seconds, 3-digit milliseconds, and a time zone offset without colons. The +0000 in the example indicates UTC. This field may be empty or not returned if no value is available.
        self.gmt_create = gmt_create
        # The last modification time of the application record. The value is returned as a string with a time zone, in the format of date, the letter T, hours-minutes-seconds, 3-digit milliseconds, and a time zone offset without colons. The +0000 in the example indicates UTC. This field may be empty or not returned if no value is available.
        self.gmt_modified = gmt_modified
        # **[Deprecated]**
        self.has_cert = has_cert
        # The icon URL of the application.
        self.icon_url = icon_url
        # The internal network icon URL of the application. Use this URL only when the corresponding network access conditions are met. The domain name in the example is for illustrative purposes only.
        self.icon_url_internal = icon_url_internal
        # The numeric ID of the application, used as the identity of the application and to associate what to do next.
        self.id = id
        # **[Deprecated]**
        self.install = install
        # **[Deprecated]**
        self.install_mode = install_mode
        # Specifies whether elevated privilege installation is configured. This does not indicate the administrator identity of the caller.
        # 
        # Valid values:
        # - true: Elevated privilege installation is configured.
        # - false: Elevated privilege installation is not configured.
        self.is_admin = is_admin
        # **[Deprecated]**
        self.is_free = is_free
        # **[Deprecated]**
        self.is_game = is_game
        # An internal field. We do not recommend that you use this field.
        self.is_white_list = is_white_list
        # **[Deprecated]**
        self.item_code = item_code
        # An internal field. We do not recommend that you use this field.
        self.labels = labels
        # An internal field. We do not recommend that you use this field.
        self.license_type = license_type
        # The English name of the management category of the application.
        self.manage_cate_en_name = manage_cate_en_name
        # The management category ID of the application, which may differ from the display category CateId.
        self.manage_cate_id = manage_cate_id
        # The management category name of the application.
        self.manage_cate_name = manage_cate_name
        # The name of the application.
        self.name = name
        # The application type.
        # 
        # Valid values:
        # - ClientBase: Client-based application.
        # - WebBase: Web-based application.
        self.origin_app_type = origin_app_type
        # **[Deprecated]**
        self.original_price = original_price
        # The operating system type of the application.
        # 
        # Valid values:
        # - WINDOWS: Windows.
        # - LINUX: Linux.
        # - ANDROID: Android.
        # - UNKNOWN: Unknown operating system.
        self.os_type = os_type
        # **[Deprecated]**
        self.owner_os = owner_os
        # **[Deprecated]**
        self.payment_type = payment_type
        # **[Deprecated]**
        self.price = price
        # **[Deprecated]**
        self.priority = priority
        # The publish time of the application. The value is returned as a string with a time zone, in the format of date, the letter T, hours-minutes-seconds, 3-digit milliseconds, and a time zone offset without colons. The +0000 in the example indicates UTC. This field may be empty or not returned if no value is available.
        self.publish_date = publish_date
        # The customer scope of the application.
        # 
        # Valid values:
        # - ENT: Enterprise.
        # - PER: Individual.
        # - BOTH: Enterprise and individual.
        self.publish_type = publish_type
        # **[Deprecated]**
        self.sandbox_mode = sandbox_mode
        # An internal field. We do not recommend that you use this field.
        self.search_tag = search_tag
        # **[Deprecated]**
        self.silence_delete_flag = silence_delete_flag
        # **[Deprecated]**
        self.silence_delete_param = silence_delete_param
        # Indicates whether silent installtion is supported. Valid values:
        # - 0: Not supported.
        # - 1: Supported.
        # 
        # This field indicates the application capability and does not represent the actual installation execute result.
        self.silence_flag = silence_flag
        # The silent installtion parameters, used by the corresponding installation flow.
        self.silence_param = silence_param
        # The size of the installation package.
        self.size = size
        # The application source. Valid values:
        # - MARKET: Alibaba Cloud Marketplace application.
        # - TENANT: Tenant-uploaded application.
        # - UNKNOWN: Unknown source.
        self.source_type = source_type
        # The start time of the application authorization. The value is returned as a string with time zone information, in the format of date, the letter T, hours-minutes-seconds, 3-digit milliseconds, and a time zone offset without colons. The +0000 in the example indicates UTC. This field may be empty or not returned if no value is available.
        self.start_time = start_time
        # The application status. This field does not represent the installation status on the endpoint. Valid values:
        # - NORMAL: Normal.
        # - DELETE: Deleted.
        # - UNCHECK: Not reviewed or not verified.
        # - DISABLE: All versions are unavailable.
        # - UNKNOWN: Unknown status.
        # 
        # **The following historical statuses from the sandbox packaging and publishing process are deprecated. Do not use them: UNPACKED (not packaged), TESTING (packaged, pending testing), UNPUBLISHED (testing completed, not published), PUBLISHED (published).**
        self.status = status
        # **[Deprecated]**
        self.sub_app_type = sub_app_type
        # The secondary source of the application. Valid values:
        # - ALI_MARKET: Alibaba Cloud Marketplace.
        # - ISV: Independent software vendor.
        # - OPS: Operations channel.
        # - UNKNOWN: Unknown source.
        self.sub_source_type = sub_source_type
        # **[Deprecated]**
        self.subscribe_count = subscribe_count
        # The account ID of the application supplier or uploader.
        self.supplier_id = supplier_id
        # An internal field. We do not recommend that you use this field.
        self.user_tag = user_tag
        # The application version number.
        self.version = version
        # The display name of the application version.
        self.version_name = version_name
        # **[Deprecated]**
        self.wam_file_name = wam_file_name
        # **[Deprecated]**
        self.wam_file_path = wam_file_path
        # **[Deprecated]**
        self.wam_file_real_name = wam_file_real_name
        # **[Deprecated]**
        self.wam_file_size = wam_file_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_tag is not None:
            result['AdminTag'] = self.admin_tag

        if self.app_admin_tag is not None:
            result['AppAdminTag'] = self.app_admin_tag

        if self.app_reg_info is not None:
            result['AppRegInfo'] = self.app_reg_info

        if self.app_tag is not None:
            result['AppTag'] = self.app_tag

        if self.app_uid is not None:
            result['AppUid'] = self.app_uid

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.auto_delete_flag is not None:
            result['AutoDeleteFlag'] = self.auto_delete_flag

        if self.auto_install_flag is not None:
            result['AutoInstallFlag'] = self.auto_install_flag

        if self.auto_install_type is not None:
            result['AutoInstallType'] = self.auto_install_type

        if self.auto_installment_type is not None:
            result['AutoInstallmentType'] = self.auto_installment_type

        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.cate_name is not None:
            result['CateName'] = self.cate_name

        if self.cluster_uid is not None:
            result['ClusterUid'] = self.cluster_uid

        if self.description is not None:
            result['Description'] = self.description

        if self.developer is not None:
            result['Developer'] = self.developer

        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price

        if self.distribute_type is not None:
            result['DistributeType'] = self.distribute_type

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.file_real_name is not None:
            result['FileRealName'] = self.file_real_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.has_cert is not None:
            result['HasCert'] = self.has_cert

        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url

        if self.icon_url_internal is not None:
            result['IconUrlInternal'] = self.icon_url_internal

        if self.id is not None:
            result['Id'] = self.id

        if self.install is not None:
            result['Install'] = self.install

        if self.install_mode is not None:
            result['InstallMode'] = self.install_mode

        if self.is_admin is not None:
            result['IsAdmin'] = self.is_admin

        if self.is_free is not None:
            result['IsFree'] = self.is_free

        if self.is_game is not None:
            result['IsGame'] = self.is_game

        if self.is_white_list is not None:
            result['IsWhiteList'] = self.is_white_list

        if self.item_code is not None:
            result['ItemCode'] = self.item_code

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.license_type is not None:
            result['LicenseType'] = self.license_type

        if self.manage_cate_en_name is not None:
            result['ManageCateEnName'] = self.manage_cate_en_name

        if self.manage_cate_id is not None:
            result['ManageCateId'] = self.manage_cate_id

        if self.manage_cate_name is not None:
            result['ManageCateName'] = self.manage_cate_name

        if self.name is not None:
            result['Name'] = self.name

        if self.origin_app_type is not None:
            result['OriginAppType'] = self.origin_app_type

        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.owner_os is not None:
            result['OwnerOs'] = self.owner_os

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.price is not None:
            result['Price'] = self.price

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.publish_date is not None:
            result['PublishDate'] = self.publish_date

        if self.publish_type is not None:
            result['PublishType'] = self.publish_type

        if self.sandbox_mode is not None:
            result['SandboxMode'] = self.sandbox_mode

        if self.search_tag is not None:
            result['SearchTag'] = self.search_tag

        if self.silence_delete_flag is not None:
            result['SilenceDeleteFlag'] = self.silence_delete_flag

        if self.silence_delete_param is not None:
            result['SilenceDeleteParam'] = self.silence_delete_param

        if self.silence_flag is not None:
            result['SilenceFlag'] = self.silence_flag

        if self.silence_param is not None:
            result['SilenceParam'] = self.silence_param

        if self.size is not None:
            result['Size'] = self.size

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_app_type is not None:
            result['SubAppType'] = self.sub_app_type

        if self.sub_source_type is not None:
            result['SubSourceType'] = self.sub_source_type

        if self.subscribe_count is not None:
            result['SubscribeCount'] = self.subscribe_count

        if self.supplier_id is not None:
            result['SupplierId'] = self.supplier_id

        if self.user_tag is not None:
            result['UserTag'] = self.user_tag

        if self.version is not None:
            result['Version'] = self.version

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        if self.wam_file_name is not None:
            result['WamFileName'] = self.wam_file_name

        if self.wam_file_path is not None:
            result['WamFilePath'] = self.wam_file_path

        if self.wam_file_real_name is not None:
            result['WamFileRealName'] = self.wam_file_real_name

        if self.wam_file_size is not None:
            result['WamFileSize'] = self.wam_file_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminTag') is not None:
            self.admin_tag = m.get('AdminTag')

        if m.get('AppAdminTag') is not None:
            self.app_admin_tag = m.get('AppAdminTag')

        if m.get('AppRegInfo') is not None:
            self.app_reg_info = m.get('AppRegInfo')

        if m.get('AppTag') is not None:
            self.app_tag = m.get('AppTag')

        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('AutoDeleteFlag') is not None:
            self.auto_delete_flag = m.get('AutoDeleteFlag')

        if m.get('AutoInstallFlag') is not None:
            self.auto_install_flag = m.get('AutoInstallFlag')

        if m.get('AutoInstallType') is not None:
            self.auto_install_type = m.get('AutoInstallType')

        if m.get('AutoInstallmentType') is not None:
            self.auto_installment_type = m.get('AutoInstallmentType')

        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')

        if m.get('ClusterUid') is not None:
            self.cluster_uid = m.get('ClusterUid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Developer') is not None:
            self.developer = m.get('Developer')

        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')

        if m.get('DistributeType') is not None:
            self.distribute_type = m.get('DistributeType')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('FileRealName') is not None:
            self.file_real_name = m.get('FileRealName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('HasCert') is not None:
            self.has_cert = m.get('HasCert')

        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')

        if m.get('IconUrlInternal') is not None:
            self.icon_url_internal = m.get('IconUrlInternal')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Install') is not None:
            self.install = m.get('Install')

        if m.get('InstallMode') is not None:
            self.install_mode = m.get('InstallMode')

        if m.get('IsAdmin') is not None:
            self.is_admin = m.get('IsAdmin')

        if m.get('IsFree') is not None:
            self.is_free = m.get('IsFree')

        if m.get('IsGame') is not None:
            self.is_game = m.get('IsGame')

        if m.get('IsWhiteList') is not None:
            self.is_white_list = m.get('IsWhiteList')

        if m.get('ItemCode') is not None:
            self.item_code = m.get('ItemCode')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')

        if m.get('ManageCateEnName') is not None:
            self.manage_cate_en_name = m.get('ManageCateEnName')

        if m.get('ManageCateId') is not None:
            self.manage_cate_id = m.get('ManageCateId')

        if m.get('ManageCateName') is not None:
            self.manage_cate_name = m.get('ManageCateName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OriginAppType') is not None:
            self.origin_app_type = m.get('OriginAppType')

        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('OwnerOs') is not None:
            self.owner_os = m.get('OwnerOs')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('PublishDate') is not None:
            self.publish_date = m.get('PublishDate')

        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')

        if m.get('SandboxMode') is not None:
            self.sandbox_mode = m.get('SandboxMode')

        if m.get('SearchTag') is not None:
            self.search_tag = m.get('SearchTag')

        if m.get('SilenceDeleteFlag') is not None:
            self.silence_delete_flag = m.get('SilenceDeleteFlag')

        if m.get('SilenceDeleteParam') is not None:
            self.silence_delete_param = m.get('SilenceDeleteParam')

        if m.get('SilenceFlag') is not None:
            self.silence_flag = m.get('SilenceFlag')

        if m.get('SilenceParam') is not None:
            self.silence_param = m.get('SilenceParam')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubAppType') is not None:
            self.sub_app_type = m.get('SubAppType')

        if m.get('SubSourceType') is not None:
            self.sub_source_type = m.get('SubSourceType')

        if m.get('SubscribeCount') is not None:
            self.subscribe_count = m.get('SubscribeCount')

        if m.get('SupplierId') is not None:
            self.supplier_id = m.get('SupplierId')

        if m.get('UserTag') is not None:
            self.user_tag = m.get('UserTag')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        if m.get('WamFileName') is not None:
            self.wam_file_name = m.get('WamFileName')

        if m.get('WamFilePath') is not None:
            self.wam_file_path = m.get('WamFilePath')

        if m.get('WamFileRealName') is not None:
            self.wam_file_real_name = m.get('WamFileRealName')

        if m.get('WamFileSize') is not None:
            self.wam_file_size = m.get('WamFileSize')

        return self

