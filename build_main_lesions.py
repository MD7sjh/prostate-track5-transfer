import pandas as pd,os,glob; d=pd.read_excel(os.environ["XLSX"],sheet_name=2,header=1); m=d.iloc[:,53].astype(str).str.contains("\u4e3b",na=False); d=d[m].copy(); rows=[]; root="/2026aicompetition/datasets/training/annotation"; 
for _,r in d.iterrows():
    acc=str(r["AccessionNumber"]); ser=str(r["SeriesUid"]); rn=str(r["RoiName"]); 
    try: num=int(float(r["RoiNumberID"]))
    except: continue
    sd=os.path.join(root,acc,ser); mp=os.path.join(sd,f"{rn}_{num}_mask.nii.gz")
    imgs=[x for x in glob.glob(os.path.join(sd,"*.nii.gz")) if "_mask.nii.gz" not in x]
    if (not os.path.exists(mp)) or len(imgs)==0: continue
    img=max(imgs,key=os.path.getsize)
    rows.append({"AccessionNumber":acc,"SeriesUid":ser,"RoiName":rn,"RoiNumberID":num,"image":img,"mask":mp,"malignancy":r.iloc[52],"capsule":r.iloc[54],"pirads":r.iloc[55],"tstage":r.iloc[57],"pathology":r.iloc[58],"fat":r.iloc[59],"nvb":r.iloc[60],"sv":r.iloc[61],"bladder":r.iloc[62],"rectal":r.iloc[63],"margin":r.iloc[64]})
pd.DataFrame(rows).to_csv("/2026aicompetition/workspace/main_lesions.csv",index=False); print("TOTAL MAIN:",len(d)); print("VALID:",len(rows))