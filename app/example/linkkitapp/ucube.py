src = Split('''
    linkkit_sample_single.c
    linkkit_entry.c
''')  # split将字符串按空白符分割成多个短语，src = ['linkkit_sample_single.c', 'linkkit_entry.c']
# linkkit_sample_gateway.c
component = aos_component('linkkitapp', src)

dependencis = Split('''
    framework/protocol/linkkit/sdk
    framework/protocol/linkkit/hal
    framework/netmgr
    framework/common
    framework/ywss4linkkit
    utility/cjson
    kernel/cli
''')  # dependencis = ['framework/protocol/linkkit/sdk', 'framework/protocol/linkkit/hal', 'framework/netmgr', 'framework/common', 'framework/ywss4linkkit', 'utility/cjson', 'kernel/cli']

for i in dependencis:
    component.add_comp_deps(i)#循环体只有这一句

global_macros = Split('''
    MQTT_DIRECT
    ALIOT_DEBUG
    IOTX_DEBUG
    USE_LPTHREAD
    TEST_ALCS
''')# global_macros = ['MQTT_DIRECT', 'ALIOT_DEBUG', 'IOTX_DEBUG', 'USE_LPTHREAD', 'TEST_ALCS']


for i in global_macros:
    component.add_global_macros(i)#循环体只有这一句

if aos_global_config.get('print_heap') == 1:
    component.add_global_macros('CONFIG_PRINT_HEAP')

if aos_global_config.mcu_family == 'esp8266':
    component.add_global_macros('ESP8266_CHIPSET')
else:
    component.add_comp_deps("cli")
