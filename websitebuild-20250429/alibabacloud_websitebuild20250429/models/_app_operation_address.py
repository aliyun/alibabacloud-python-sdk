# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class AppOperationAddress(DaraModel):
    def __init__(
        self,
        actions: List[main_models.AppOperateAction] = None,
        ai_customer_config_url: str = None,
        ai_design_url: str = None,
        app_publish_url: str = None,
        dashboard_actions: List[main_models.AppOperateAction] = None,
        design_url: str = None,
        instance_login_url: str = None,
        renew_buy_url: str = None,
        server_delivery_url: str = None,
        upgrade_buy_url: str = None,
    ):
        self.actions = actions
        self.ai_customer_config_url = ai_customer_config_url
        self.ai_design_url = ai_design_url
        self.app_publish_url = app_publish_url
        self.dashboard_actions = dashboard_actions
        self.design_url = design_url
        self.instance_login_url = instance_login_url
        self.renew_buy_url = renew_buy_url
        self.server_delivery_url = server_delivery_url
        self.upgrade_buy_url = upgrade_buy_url

    def validate(self):
        if self.actions:
            for v1 in self.actions:
                 if v1:
                    v1.validate()
        if self.dashboard_actions:
            for v1 in self.dashboard_actions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Actions'] = []
        if self.actions is not None:
            for k1 in self.actions:
                result['Actions'].append(k1.to_map() if k1 else None)

        if self.ai_customer_config_url is not None:
            result['AiCustomerConfigUrl'] = self.ai_customer_config_url

        if self.ai_design_url is not None:
            result['AiDesignUrl'] = self.ai_design_url

        if self.app_publish_url is not None:
            result['AppPublishUrl'] = self.app_publish_url

        result['DashboardActions'] = []
        if self.dashboard_actions is not None:
            for k1 in self.dashboard_actions:
                result['DashboardActions'].append(k1.to_map() if k1 else None)

        if self.design_url is not None:
            result['DesignUrl'] = self.design_url

        if self.instance_login_url is not None:
            result['InstanceLoginUrl'] = self.instance_login_url

        if self.renew_buy_url is not None:
            result['RenewBuyUrl'] = self.renew_buy_url

        if self.server_delivery_url is not None:
            result['ServerDeliveryUrl'] = self.server_delivery_url

        if self.upgrade_buy_url is not None:
            result['UpgradeBuyUrl'] = self.upgrade_buy_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k1 in m.get('Actions'):
                temp_model = main_models.AppOperateAction()
                self.actions.append(temp_model.from_map(k1))

        if m.get('AiCustomerConfigUrl') is not None:
            self.ai_customer_config_url = m.get('AiCustomerConfigUrl')

        if m.get('AiDesignUrl') is not None:
            self.ai_design_url = m.get('AiDesignUrl')

        if m.get('AppPublishUrl') is not None:
            self.app_publish_url = m.get('AppPublishUrl')

        self.dashboard_actions = []
        if m.get('DashboardActions') is not None:
            for k1 in m.get('DashboardActions'):
                temp_model = main_models.AppOperateAction()
                self.dashboard_actions.append(temp_model.from_map(k1))

        if m.get('DesignUrl') is not None:
            self.design_url = m.get('DesignUrl')

        if m.get('InstanceLoginUrl') is not None:
            self.instance_login_url = m.get('InstanceLoginUrl')

        if m.get('RenewBuyUrl') is not None:
            self.renew_buy_url = m.get('RenewBuyUrl')

        if m.get('ServerDeliveryUrl') is not None:
            self.server_delivery_url = m.get('ServerDeliveryUrl')

        if m.get('UpgradeBuyUrl') is not None:
            self.upgrade_buy_url = m.get('UpgradeBuyUrl')

        return self

