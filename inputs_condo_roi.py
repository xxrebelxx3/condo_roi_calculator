

print("Enter whole numbers without a , $ or %")
# variables
condo_cost = int(input("Enter cost of condo in USD: "))
nightly_rent = int(input("Enter nightly rental list price in USD: "))
cleaning_fee = int(input("Enter the nightly cleaning fee, enter zero if charging this to guest: "))
closing_pct = int(input("Enter closing cost percent: "))
yearly_tax_pct = int(input("Enter yearly property tax as a percentage of property value: "))
property_mgmt_pct = int(input("Enter property management fee as percent of nightly rate: "))
listing_pct = int(input("Enter fee charged by rental listing platform as percent per nightly rate: "))
occupancy_rate = int(input("Enter occupancy rate as a percent: "))
insurance_yearly = int(input("Enter yearly insurance cost: "))
company_formation = int(input("Enter cost of incorporation: "))

yearly_rev = nightly_rent * 365 * (occupancy_rate / 100)

yearly_cost = (cleaning_fee * 365 * (occupancy_rate / 100)) + (condo_cost * (yearly_tax_pct / 100)) + ((nightly_rent * (property_mgmt_pct / 100)) + (nightly_rent * (listing_pct / 100)) * 365 * (occupancy_rate / 100)) + insurance_yearly

final_cost = condo_cost + (condo_cost * closing_pct / 100) + company_formation

yearly_net = yearly_rev - yearly_cost

yearly_roi_pct = yearly_net / final_cost * 100

roi = final_cost / yearly_net

print("final cost: ", final_cost)
print("yearly roi: ", yearly_roi_pct)
print("years until roi: ", roi)



