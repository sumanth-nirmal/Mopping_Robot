################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Each subdirectory must supply rules for building sources it contributes
Source/portable/GCC/ARM_CM3_MPU/port.obj: ../Source/portable/GCC/ARM_CM3_MPU/port.c $(GEN_OPTS) $(GEN_HDRS)
	@echo 'Building file: $<'
	@echo 'Invoking: ARM Compiler'
	"C:/ti/ccsv6/tools/compiler/ti-cgt-arm_5.2.5/bin/armcl" -mv7M4 --code_state=16 --float_support=FPv4SPD16 --abi=eabi -me --include_path="C:/ti/ccsv6/tools/compiler/ti-cgt-arm_5.2.5/include" --include_path="C:/ti/TivaWare_C_Series-2.1.2.111/third_party/FreeRTOS" --include_path="C:/ti/TivaWare_C_Series-2.1.2.111/third_party" --include_path="C:/ti/TivaWare_C_Series-2.1.2.111/third_party/FreeRTOS/Source/portable/CCS/ARM_CM4F" --include_path="C:/D Drive/Start up/cleaner mob/workspace/MOPPING_BOT" --include_path="C:/ti/TivaWare_C_Series-2.1.2.111" --include_path="C:/ti/TivaWare_C_Series-2.1.2.111/third_party/FreeRTOS/Source/include" -g --gcc --define=ccs="ccs" --define=TARGET_IS_TM4C123_RB1 --define=PART_TM4C123GH6PM --display_error_number --diag_warning=225 --diag_wrap=off --preproc_with_compile --preproc_dependency="Source/portable/GCC/ARM_CM3_MPU/port.pp" --obj_directory="Source/portable/GCC/ARM_CM3_MPU" $(GEN_OPTS__FLAG) "$<"
	@echo 'Finished building: $<'
	@echo ' '


