# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckAddRegionToExpressConnectRouterResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        any_cross_border_link: bool = None,
        any_inter_region_link: bool = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        is_cdt_cross_border_enabled: bool = None,
        is_cdt_inter_region_enabled: bool = None,
        is_user_allowed_to_create_cross_border_link: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # Indicates whether the ECR is used to establish connections between regions in the Chinese mainland and regions outside China. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.any_cross_border_link = any_cross_border_link
        # Indicates whether the ECR is used to establish connections between regions in the Chinese mainland. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.any_inter_region_link = any_inter_region_link
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsInstanceId**, the request parameter **DtsInstanceId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # Indicates whether the cross-border CDT service is activated for the account to which the ECR belongs. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_cdt_cross_border_enabled = is_cdt_cross_border_enabled
        # Indicates whether the CDT service is activated for the account to which the ECR belongs. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_cdt_inter_region_enabled = is_cdt_inter_region_enabled
        # Indicates whether the account to which the ECR belongs can create cross-border connections. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_user_allowed_to_create_cross_border_link = is_user_allowed_to_create_cross_border_link
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.any_cross_border_link is not None:
            result['AnyCrossBorderLink'] = self.any_cross_border_link

        if self.any_inter_region_link is not None:
            result['AnyInterRegionLink'] = self.any_inter_region_link

        if self.code is not None:
            result['Code'] = self.code

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.is_cdt_cross_border_enabled is not None:
            result['IsCdtCrossBorderEnabled'] = self.is_cdt_cross_border_enabled

        if self.is_cdt_inter_region_enabled is not None:
            result['IsCdtInterRegionEnabled'] = self.is_cdt_inter_region_enabled

        if self.is_user_allowed_to_create_cross_border_link is not None:
            result['IsUserAllowedToCreateCrossBorderLink'] = self.is_user_allowed_to_create_cross_border_link

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AnyCrossBorderLink') is not None:
            self.any_cross_border_link = m.get('AnyCrossBorderLink')

        if m.get('AnyInterRegionLink') is not None:
            self.any_inter_region_link = m.get('AnyInterRegionLink')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('IsCdtCrossBorderEnabled') is not None:
            self.is_cdt_cross_border_enabled = m.get('IsCdtCrossBorderEnabled')

        if m.get('IsCdtInterRegionEnabled') is not None:
            self.is_cdt_inter_region_enabled = m.get('IsCdtInterRegionEnabled')

        if m.get('IsUserAllowedToCreateCrossBorderLink') is not None:
            self.is_user_allowed_to_create_cross_border_link = m.get('IsUserAllowedToCreateCrossBorderLink')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

