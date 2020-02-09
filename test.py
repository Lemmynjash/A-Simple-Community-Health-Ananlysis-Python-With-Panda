import pandas as pd


def main():
    print("am here")
    socioEconExcel_file = 'TheSocio.xlsx'
    socioEcon = pd.read_excel(socioEconExcel_file)
    socioEcon.head()

    livingsettings_file = 'LivingSettings.xlsx'
    livingSettings = pd.read_excel(livingsettings_file)
    livingSettings.head()

    theChvs_file = 'TheChvProfiles.xlsx'
    theChvs = pd.read_excel(theChvs_file)
    theChvs.head()

    theCounty_file = 'theCounties.xlsx'
    theCounties = pd.read_excel(theCounty_file)
    theCounties.head()

    for index, socio in socioEcon.iterrows():

        print(index, socio['SocioEconomicId'], socio['Name'], socio['ChvDetail'])

        TotalExpe = (socio['FoodExpenditure'] + socio['EducationExpenditure'] +
                     socio['MedicationExpenditure'] + socio['AirtimeExpenditure'] +
                     socio['UtilityExpenditure'])

        TotalInc = (int(socio['AvrgIncome']) - TotalExpe)

        for indextwo, chvs in theChvs.iterrows():
            print(indextwo, chvs['UserName'], chvs['UserPhone'], chvs['County'])

            if str(socio['ChvDetail']).startswith('7'):
                theChvNo="0"+str(socio['ChvDetail'])
                if str(chvs['UserPhone']) == theChvNo:
                    print(chvs['UserName'])
                    for indexthree, myCounties in theCounties.iterrows():
                        print(myCounties['CountyName'])
                        if myCounties['countyId'] == chvs['County']:
                            print(myCounties['CountyName'])
                            print(myCounties['SettingId'])
                            if myCounties['SettingId'] == 1.0:
                                print("Calculating Rural for County ", myCounties['CountyName'])
                                if (TotalInc < 1):
                                    inc = 0.125
                                else:
                                    inc = 0
                                if socio['Disabled'] == "Yes" or socio['AnyDisabledMembers'] == "Yes":
                                    dsbld = 0.125
                                else:
                                    dsbld = 0
                                if socio['MembersOverSixtyFive'] > 0 or socio['MembersOverSeventy'] > 0:
                                    memage = 0.125
                                else:
                                    memage = 0
                                if socio['EducationLevel'] == "None":
                                    edu = 0.25
                                else:
                                    edu = 0
                                if socio['SafeWater'] == "No":
                                    safew = 0.04166667
                                else:
                                    safew = 0
                                if socio['FunctionalLatrine'] == "No":
                                    functionalLat = 0.01388889
                                else:
                                    functionalLat = 0
                                if ['RefuseDisposal'] == "No":
                                    refusedisp = 0.01388889
                                else:
                                    refusedisp = 0

                                if socio['Handwashing'] == "No":
                                    handwash = 0.01388889
                                else:
                                    handwash = 0
                                if socio['CookingFuelSource'] == "Charcoal" or socio['CookingFuelSource'] == "Firewood":
                                    cooking = 0.04166667
                                else:
                                    cooking = 0

                                if socio['LightingSource'] == "Kerosine Lamp" or socio['LightingSource'] == "Koroboi":
                                    lightsource = 0.04166667
                                else:
                                    lightsource = 0

                                if socio['FloorMaterial'] == "Cement":
                                    floortype = 0
                                else:
                                    floortype = 0.04166667

                                if socio['Beds'] == "No" or socio['HaveVehicle'] == "No":
                                    bed = 0.01388889
                                else:
                                    bed = 0

                                if (socio['Cows'] > 0 or socio['Goats'] > 0 or
                                        socio['Sheep'] > 0 or socio['Donkey'] > 0 or socio['Chicken'] > 0 or socio['Camel'] > 0):
                                    farmproduce = 0
                                else:
                                    farmproduce = 0.01388889

                                if socio['Landsize'] > 0:
                                    land = 0
                                else:
                                    land = 0.01388889

                                if socio['EmpStatus'] == "Unemployed":
                                    emp = 0.125
                                else:
                                    emp = 0
                            elif myCounties['SettingId'] == 2.0:
                                print("Calculating Urban for County ", myCounties['CountyName'])
                                if TotalInc < 1:
                                    inc = 0.125
                                else:
                                    inc = 0
                                if socio['Disabled'] == "Yes" or socio['AnyDisabledMembers'] == "Yes":
                                    dsbld = 0.125
                                else:
                                    dsbld = 0

                                if socio['MembersOverSixtyFive'] > 0 or socio['MembersOverSeventy'] > 0:
                                    memage = 0.125
                                else:
                                    memage = 0

                                if socio['EducationLevel'] == "None":
                                    edu = 0.25
                                else:
                                    edu = 0

                                if socio['SafeWater'] == "No":
                                    safew = 0.04166667
                                else:
                                    safew = 0

                                if socio['FunctionalLatrine'] == "No":
                                    functionalLat = 0.01388889
                                else:
                                    functionalLat = 0

                                if socio['RefuseDisposal'] == "No":
                                    refusedisp = 0.01388889
                                else:
                                    refusedisp = 0

                                if socio['Handwashing'] == "No":
                                    handwash = 0.01388889
                                else:
                                    handwash = 0

                                if socio['CookingFuelSource'] == "Charcoal" or socio['CookingFuelSource'] == "Firewood":
                                    cooking = 0.04166667
                                else:
                                    cooking = 0

                                if socio['LightingSource'] == "Kerosine Lamp" or socio['LightingSource'] == "Koroboi":
                                    lightsource = 0.04166667
                                else:
                                    lightsource = 0

                                if socio['FloorMaterial'] == "Cement":
                                    floortype = 0
                                else:
                                    floortype = 0.04166667

                                if socio['Beds'] == "No" or socio['HaveVehicle'] == "No":
                                    bed = 0.02083333
                                else:
                                    bed = 0

                                if socio['Landsize'] > 0:
                                    land = 0
                                else:
                                    land = 0.02083333

                                if socio['EmpStatus'] == "Unemployed":
                                    emp = 0.125
                                else:
                                    emp = 0
                            else:
                                print("Calculating Urban for County ", myCounties['CountyName'])
                                if TotalInc < 1:
                                    inc = 0.125
                                else:
                                    inc = 0
                                if socio['Disabled'] == "Yes" or socio['AnyDisabledMembers'] == "Yes":
                                    dsbld = 0.125
                                else:
                                    dsbld = 0

                                if socio['MembersOverSixtyFive'] > 0 or socio['MembersOverSeventy'] > 0:
                                    memage = 0.125
                                else:
                                    memage = 0

                                if socio['EducationLevel'] == "None":
                                    edu = 0.25
                                else:
                                    edu = 0

                                if socio['SafeWater'] == "No":
                                    safew = 0.04166667
                                else:
                                    safew = 0

                                if socio['FunctionalLatrine'] == "No":
                                    functionalLat = 0.01388889
                                else:
                                    functionalLat = 0

                                if socio['RefuseDisposal'] == "No":
                                    refusedisp = 0.01388889
                                else:
                                    refusedisp = 0

                                if socio['Handwashing'] == "No":
                                    handwash = 0.01388889
                                else:
                                    handwash = 0

                                if socio['CookingFuelSource'] == "Charcoal" or socio['CookingFuelSource'] == "Firewood":
                                    cooking = 0.04166667
                                else:
                                    cooking = 0

                                if socio['LightingSource'] == "Kerosine Lamp" or socio['LightingSource'] == "Koroboi":
                                    lightsource = 0.04166667
                                else:
                                    lightsource = 0

                                if socio['FloorMaterial'] == "Cement":
                                    floortype = 0
                                else:
                                    floortype = 0.04166667

                                if socio['Beds'] == "No" or socio['HaveVehicle'] == "No":
                                    bed = 0.01388889
                                else:
                                    bed = 0

                                if (socio['Cows'] > 0 or socio['Goats'] > 0 or
                                        socio['Sheep'] > 0 or socio['Donkey'] > 0 or socio['Chicken'] > 0 or socio['Camel'] > 0):
                                    farmproduce = 0
                                else:
                                    farmproduce = 0.01388889

                                if socio['Landsize'] > 0:
                                    land = 0
                                else:
                                    land = 0.01388889

                                if socio['EmpStatus'] == "Unemployed":
                                    emp = 0.125
                                else:
                                    emp = 0

                            myPovertyList = []
                            PtyIndex = (dsbld + memage + edu + safew +
                                        functionalLat + refusedisp + handwash +
                                        cooking + lightsource + floortype + bed +
                                        farmproduce + land + emp + inc)

                            if PtyIndex <= 0.3:
                                PovertyIndex = 0
                                myPovertyList.append(PovertyIndex)
                            elif 0.3 < PtyIndex <= 0.475:
                                PovertyIndex = 1
                                myPovertyList.append(PovertyIndex)
                            elif 0.475 < PtyIndex <= 0.65:
                                PovertyIndex = 2
                                myPovertyList.append(PovertyIndex)
                            elif 0.65 < PtyIndex <= 0.825:
                                PovertyIndex = 3
                                myPovertyList.append(PovertyIndex)
                            elif PtyIndex > 0.825:
                                PovertyIndex = 4
                                myPovertyList.append(PovertyIndex)
                            else:
                                PovertyIndex = 5
                                myPovertyList.append(PovertyIndex)

                            finalSocio = socioEcon.assign(MyStatusPovertyIndex=myPovertyList)
                            finalSocio.head()
                        else:
                            print("County does not exist")
                else:
                    print("Chv details does not exist")
            else:
                print("Doesnt start with zero")


if __name__ == '__main__':
    main()
